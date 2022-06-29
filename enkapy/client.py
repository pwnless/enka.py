import json

import aiohttp
from aiocache import cached

from .exception import ValidateUIDError, UIDNotFounded
from .model import EnkaData
from .model.artifact import Artifact


class Enka:
    URL = "https://enka.shinshin.moe/u/{uid}/__data.json"
    LANG_URL = 'https://raw.githubusercontent.com/Dimbreath/GenshinData/master/TextMap/TextMap{lang}.json'
    AVATAR_URL = 'https://raw.githubusercontent.com/Dimbreath/GenshinData/master/ExcelBinOutput/AvatarExcelConfigData.json'
    USER_AGENT = "Mozilla/5.0"
    timeout = 5
    proxy = ''
    lang_data = {}
    avatar_data = {}
    lang = 'en'

    async def load_lang(self, lang='en'):
        async with aiohttp.ClientSession(headers={"User-Agent": self.USER_AGENT}) as client:
            if lang not in self.lang_data:
                resp = await client.get(self.LANG_URL.format(lang=lang.upper()), proxy=self.proxy)
                self.lang_data[lang] = json.loads(await resp.text())
            if not self.avatar_data:
                resp = await client.get(self.AVATAR_URL, proxy=self.proxy)
                for x in json.loads(await resp.text()):
                    self.avatar_data[x['id']] = x

    async def resolve_text_hash(self, text_hash, lang='en'):
        if lang not in self.lang_data:
            await self.load_lang(lang)
        if not isinstance(text_hash, str):
            text_hash = str(text_hash)
        if text_hash in self.lang_data[lang]:
            return self.lang_data[lang][text_hash]
        else:
            return ''

    @cached(ttl=600)
    async def fetch_user(self, uid: int) -> EnkaData:
        if not isinstance(uid, int):
            try:
                uid = int(uid)
            except ValueError:
                raise ValidateUIDError("Validate UID failed. Please check your UID.")
        if len(str(uid)) != 9 or (100000000 > uid > 999999999):
            raise ValidateUIDError("Validate UID failed. Please check your UID.")

        async with aiohttp.ClientSession(headers={"User-Agent": self.USER_AGENT},
                                         timeout=aiohttp.ClientTimeout(total=self.timeout)) as client:
            resp = await client.get(self.URL.format(uid=uid), proxy=self.proxy)

            if resp.status != 200:
                raise UIDNotFounded(f"UID {uid} not found.")

            data = await resp.json()

            if not data:
                raise UIDNotFounded(f"UID {uid} not found.")

        obj = EnkaData.parse_obj(data)
        if self.lang and self.lang_data[self.lang] and self.avatar_data:
            for character in obj.characters:
                for equip in character.equipList:
                    equip.flat.nameText = await self.resolve_text_hash(equip.flat.nameTextMapHash, self.lang)
                    if isinstance(equip, Artifact):
                        equip.flat.setNameText = await self.resolve_text_hash(equip.flat.setNameTextMapHash, self.lang)
                if character.id in self.avatar_data:
                    character.name = await self.resolve_text_hash(self.avatar_data[character.id]['nameTextMapHash'], self.lang)
        return obj
