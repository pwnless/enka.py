# Enka.py
[![Downloads](https://static.pepy.tech/badge/enka-py)](https://pepy.tech/project/enka-py) [![Downloads](https://static.pepy.tech/badge/enka-py/month)](https://pepy.tech/project/enka-py) ![](https://img.shields.io/pypi/v/enka.py)

Friendly API for fetching genshin user data from https://enka.shinshin.moe/ (Now https://enka.network)

Added name parsing and full artifact support and more elegant code.

original from https://github.com/mrwan200/EnkaNetwork.py, but better!

# Documentation

see http://enkapy.rtfd.io/

# Installation
```
pip install enka.py
```

# Usage
```py
import asyncio

from enkapy import Enka

client = Enka()


async def main():
    await client.load_lang()
    user = await client.fetch_user(104267816)
    print(f"Nickname: {user.player.nickname}")
    print(f"Level: {user.player.level}")
    print(f'Signature: {user.player.signature}')
    print(f'World level:{user.player.worldLevel}')
    print(f'Abyss: {user.player.towerFloorIndex}-{user.player.towerLevelIndex}')
    # fetch first character
    character = user.characters[0]
    print(f'Name: {character.name}')
    print(f'Ascension: {character.ascension}')
    print(f'Level: {character.level}')
    print(f'Exp: {character.experience}')
    print('Weapon:')
    weapon = character.weapon
    print(f'\tName: {weapon.name}')
    print(f'\tLevel: {weapon.level}')
    print(f'\tRefine: {weapon.refine}')
    print(f'\tStar level: {weapon.rank}')

    print('Constellations:')
    for constellation in character.constellations:
        if constellation.activated:
            print(f'\t{constellation.name} Activated')
    print('Skills:')
    for skill in character.skills:
        if skill.type == 0:
            print(f'\tNormal skill {skill.name}, level:{skill.level}')
        elif skill.type == 1:
            print(f'\tElemental skill {skill.name}, level:{skill.level}')
        elif skill.type == 2:
            print(f'\tElemental burst {skill.name}, level:{skill.level}')
    print('Artifacts:')
    for artifact in character.artifacts:
        print(f'\t{artifact.set_name} {artifact.name}:')
        print(f'\t{artifact.main_stat.prop}:{artifact.main_stat.value}')
        for sub_stats in artifact.sub_stats:
            print(f'\t\t{sub_stats.prop}:{sub_stats.value}')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
Result:
```sh
Nickname: 天天向上
Level: 60
Signature: 凌人有点无脑
World level:8
Abyss: 12-3
Name: Kamisato Ayaka
Ascension: 6
Level: 90
Exp: 0
Weapon:
    Name: Mistsplitter Reforged
    Level: 90
    Refine: 5
    Star level: 5
Constellations:
    Snowswept Sakura Activated
    Blizzard Blade Seki no To Activated
    Frostbloom Kamifubuki Activated
    Ebb and Flow Activated
    Blossom Cloud Irutsuki Activated
    Dance of Suigetsu Activated
Skills:
    Elemental burst Kamisato Art: Soumetsu, level:10
    Normal skill Normal Attack: Kamisato Art - Kabuki, level:10
    Elemental skill Kamisato Art: Hyouka, level:9
    Normal skill Kamisato Art: Senho, level:1
Artifacts:
    Blizzard Strayer Snowswept Memory:
    FIGHT_PROP_HP:4780.0
        FIGHT_PROP_ELEMENT_MASTERY:44.0
        FIGHT_PROP_CRITICAL_HURT:38.1
        FIGHT_PROP_DEFENSE:16.0
        FIGHT_PROP_CRITICAL:3.9
    Blizzard Strayer Icebreaker's Resolve:
    FIGHT_PROP_ATTACK:311.0
        FIGHT_PROP_CRITICAL:3.1
        FIGHT_PROP_ELEMENT_MASTERY:35.0
        FIGHT_PROP_CHARGE_EFFICIENCY:10.4
        FIGHT_PROP_CRITICAL_HURT:21.8
    Blizzard Strayer Frozen Homeland's Demise:
    FIGHT_PROP_ATTACK_PERCENT:46.6
        FIGHT_PROP_HP_PERCENT:8.7
        FIGHT_PROP_ATTACK:18.0
        FIGHT_PROP_CRITICAL_HURT:13.2
        FIGHT_PROP_CRITICAL:10.5
    Archaic Petra Goblet of Chiseled Crag:
    FIGHT_PROP_ICE_ADD_HURT:46.6
        FIGHT_PROP_ELEMENT_MASTERY:16.0
        FIGHT_PROP_CRITICAL_HURT:25.7
        FIGHT_PROP_HP_PERCENT:10.5
        FIGHT_PROP_CRITICAL:5.4
    Blizzard Strayer Broken Rime's Echo:
    FIGHT_PROP_CRITICAL_HURT:62.2
        FIGHT_PROP_CRITICAL:11.7
        FIGHT_PROP_ATTACK_PERCENT:9.3
        FIGHT_PROP_ELEMENT_MASTERY:42.0
        FIGHT_PROP_DEFENSE:35.0
```

If you want full docs for the API, visit [EnkaNetwork API](https://github.com/EnkaNetwork/API-docs)

# LICENSE
[MIT License](./LICENSE)
