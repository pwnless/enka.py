import json
import os.path

import aiohttp
from aiocache import cached

from .exception import *
from .model import EnkaData
from .model.artifact import Artifact
from .model.character import CharacterSkill, CharacterConstellation, CharacterSkillType


class Enka:
    """
    Main Enka object.

    Example::

        user = await client.fetch_user(104267816)
        print(f"Nickname: {user.player.nickname}")

    """
    _URL = "https://enka.network/api/uid/{uid}"
    # https://github.com/theBowja/GenshinData-1
    # https://raw.githubusercontent.com/GrownNed/Homework/master
    _REPO_BASE = 'https://gitlab.com/Dimbreath/gamedata/-/raw/master'
    _LANG_URL = _REPO_BASE + '/TextMap/TextMap{lang}.json?inline=false'
    _AVATAR_URL = _REPO_BASE + '/ExcelBinOutput/AvatarExcelConfigData.json?inline=false'
    _TALENT_URL = _REPO_BASE + '/ExcelBinOutput/AvatarTalentExcelConfigData.json?inline=false'
    _SKILL_DEPOT_URL = _REPO_BASE + '/ExcelBinOutput/AvatarSkillDepotExcelConfigData.json?inline=false'
    _SKILL_URL = _REPO_BASE + '/ExcelBinOutput/AvatarSkillExcelConfigData.json?inline=false'
    USER_AGENT = "Mozilla/5.0"
    timeout = 30
    """Http connection timeout"""
    proxy = ''
    """Http connection proxy"""
    _lang_data = {}
    """Internal language data"""
    _avatar_data = {}
    """Internal avatar data"""
    _talent_data = {}
    """Internal talent data"""
    _skill_depot_data = {}
    """Internal skill pot data"""
    _skill_data = {}
    """Internal skill data"""
    lang = 'en'
    """Language for text hash resolve"""
    _cache = 'cache'
    """Cache folder name"""

    def _cache_exists(self, name):
        """
        Check if cache file exists and return full cache file path

        :param name: cache name
        :return: full cache file path
        """
        package_path = os.path.dirname(os.path.realpath(__file__))
        cache_path = os.path.join(package_path, self._cache)
        cache_file_path = os.path.join(cache_path, name)

        if not os.path.exists(cache_path):
            try:
                os.mkdir(cache_path)
            except OSError:
                pass
            return ''
        if not os.path.isdir(cache_path):
            try:
                os.remove(cache_path)
            except OSError:
                pass
            return ''
        if os.path.exists(cache_file_path):
            return cache_file_path
        else:
            return ''

    async def _process_cache(self, client: aiohttp.ClientSession, url, cache_file, force_cache=False,
                             force_update=False):
        """
        Process cache

        :param client: aiohttp client
        :param url: git url
        :param cache_file: cache file name
        :param force_cache: ignore git update, force using cache file
        :param force_update: force update from git repo
        :return: cache file path
        """
        cache_file_path = self._cache_exists(cache_file)
        if cache_file_path and not force_update:
            stat = os.stat(cache_file_path)
            file_size = stat.st_size
            if not force_cache:
                resp = await client.head(url, proxy=self.proxy)
                cl = int(resp.headers['Content-Length'])
                if cl != file_size:
                    resp = await client.get(url, proxy=self.proxy)
                    with open(cache_file_path, 'wb') as f:
                        f.write(await resp.read())
        else:
            package_path = os.path.dirname(os.path.realpath(__file__))
            cache_path = os.path.join(package_path, self._cache)
            cache_file_path = os.path.join(cache_path, cache_file)
            resp = await client.get(url, proxy=self.proxy)
            with open(cache_file_path, 'wb') as f:
                f.write(await resp.read())
        return cache_file_path

    async def load_lang(self, lang='en', force_cache=False, force_update=False):
        """
        Load language data from cache or Dimbreath repo

        :param lang: language you want to load, default 'en'
        :param force_cache: Do not check repo update if cache file exists
        :param force_update: force update from git repo
        """

        async with aiohttp.ClientSession(headers={"User-Agent": self.USER_AGENT}) as client:
            if lang not in self._lang_data:
                cache_file_path = await self._process_cache(client,
                                                            self._LANG_URL.format(lang=lang.upper()),
                                                            'lang.json',
                                                            force_cache,
                                                            force_update)
                with open(cache_file_path, 'rb') as f:
                    self._lang_data[lang] = json.load(f)
            if not self._avatar_data:
                cache_file_path = await self._process_cache(client,
                                                            self._AVATAR_URL,
                                                            'avatar.json',
                                                            force_cache,
                                                            force_update)
                with open(cache_file_path, 'rb') as f:
                    for x in json.load(f):
                        self._avatar_data[x['id']] = x
            if not self._skill_depot_data:
                cache_file_path = await self._process_cache(client,
                                                            self._SKILL_DEPOT_URL,
                                                            'skill_depot.json',
                                                            force_cache,
                                                            force_update)
                with open(cache_file_path, 'rb') as f:
                    for x in json.load(f):
                        self._skill_depot_data[x['id']] = x
            if not self._skill_data:
                cache_file_path = await self._process_cache(client,
                                                            self._SKILL_URL,
                                                            'skill.json',
                                                            force_cache,
                                                            force_update)
                with open(cache_file_path, 'rb') as f:
                    for x in json.load(f):
                        self._skill_data[x['id']] = x
            if not self._talent_data:
                cache_file_path = await self._process_cache(client,
                                                            self._TALENT_URL,
                                                            'talent.json',
                                                            force_cache,
                                                            force_update)
                with open(cache_file_path, 'rb') as f:
                    for x in json.load(f):
                        self._talent_data[x['talentId']] = x

    async def resolve_text_hash(self, text_hash, lang='en'):
        """
        Resolve text hash to actual text

        :param text_hash: text hash
        :param lang: language you want to resolve to
        :return: resolved text
        """
        if lang not in self._lang_data:
            await self.load_lang(lang)
        if not isinstance(text_hash, str):
            text_hash = str(text_hash)
        if text_hash in self._lang_data[lang]:
            return self._lang_data[lang][text_hash]
        else:
            return ''

    @cached(ttl=600)
    async def fetch_user(self, uid: int, player_only=False) -> EnkaData:
        """
        Fetch user data from enka api, resolve text hash if available

        :param uid: user in game uid
        :param player_only: fetch only player info
        :return: EnkaData object referencing player
        """
        if not isinstance(uid, int):
            try:
                uid = int(uid)
            except ValueError:
                raise ValidateUIDError("Validate UID failed. Please check your UID.")
        if len(str(uid)) != 9 or (100000000 > uid > 999999999):
            raise ValidateUIDError("Validate UID failed. Please check your UID.")

        async with aiohttp.ClientSession(headers={"User-Agent": self.USER_AGENT},
                                         timeout=aiohttp.ClientTimeout(total=self.timeout)) as client:
            url = self._URL.format(uid=uid)
            if player_only:
                url += '?info'
            resp = await client.get(url, proxy=self.proxy)

            if resp.status != 200:
                if resp.status == 400:
                    raise WrongUIDFormat(f'Wrong uid format! {uid}')
                elif resp.status == 404:
                    raise PlayerDoesNOTExist(f'Player {uid} does not exist')
                elif resp.status == 424:
                    raise GameMaintenance('Game in maintenance')
                elif resp.status == 429:
                    raise RateLimited('Rate limited')
                elif resp.status == 500:
                    raise GeneralServerError('Server error 500')
                elif resp.status == 503:
                    raise EnkaError('Enka endpoint error 503')
                else:
                    raise EnkaError(f'Unknown error {resp.status}')

            data = await resp.json()

            if not data:
                raise EnkaError(f'Unknown error[No Data]')

        obj: EnkaData = EnkaData.parse_obj(data)

        if not player_only:
            for character in obj.characters:
                if character.skill_depot_id in self._skill_depot_data:
                    depot = self._skill_depot_data[character.skill_depot_id]
                    if 'energySkill' in depot:
                        burst_id = depot['energySkill']
                        if burst_id in self._skill_data:
                            cs = CharacterSkill()
                            cs.id = burst_id
                            cs.type = CharacterSkillType.ElementalBurst
                            cs.name_hash = self._skill_data[burst_id]['nameTextMapHash']
                            cs.icon = self._skill_data[burst_id]['skillIcon']
                            character.skills.append(cs)
                    for skill_id in depot['skills']:
                        if skill_id and skill_id in self._skill_data:
                            skill_info = self._skill_data[skill_id]
                            cs = CharacterSkill()
                            cs.id = skill_id
                            if 'cdTime' in skill_info and skill_info['cdTime']:
                                cs.type = CharacterSkillType.ElementalSkill
                            else:
                                cs.type = CharacterSkillType.NormalSkill
                            cs.name_hash = skill_info['nameTextMapHash']
                            cs.icon = self._skill_data[burst_id]['skillIcon']
                            character.skills.append(cs)
                    for talent_id in depot['talents']:
                        if talent_id and talent_id in self._talent_data:
                            talent_info = self._talent_data[talent_id]
                            tl = CharacterConstellation()
                            tl.id = talent_id
                            tl.icon = talent_info['icon']
                            tl.name_hash = talent_info['nameTextMapHash']
                            character.constellations.append(tl)
                    character.process_skill()
                    character.activate_constellation()
                if self.lang and self.lang in self._lang_data and self._lang_data[self.lang] and self._avatar_data:
                    for equip in character.equipList:
                        equip.flat.nameText = await self.resolve_text_hash(equip.flat.nameTextMapHash, self.lang)
                        if isinstance(equip, Artifact):
                            equip.flat.setNameText = await self.resolve_text_hash(equip.flat.setNameTextMapHash,
                                                                                  self.lang)
                    if character.id in self._avatar_data:
                        character.name = await self.resolve_text_hash(
                            self._avatar_data[character.id]['nameTextMapHash'],
                            self.lang)
                    for skill in character.skills:
                        skill.name = await self.resolve_text_hash(skill.name_hash, self.lang)
                    for c in character.constellations:
                        c.name = await self.resolve_text_hash(c.name_hash, self.lang)
        return obj
