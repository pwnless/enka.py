# Enka.py
Friendly API for fetching genshin user data from https://enka.shinshin.moe/

Added name parsing and full artifact support and more elegant code.

original from https://github.com/mrwan200/EnkaNetwork.py

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
    for character in user.characters:
        print(f'Name: {character.name}')
        print(f'Weapon: {character.weapon.nameText}')
        print('Artifacts:')
        for artifact in character.artifacts:
            print(f'\t{artifact.setNameText} {artifact.nameText}:')
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
   Name: Kamisato Ayaka
   Weapon: Mistsplitter Reforged
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
   Name: Yelan
   Weapon: Aqua Simulacra
   Artifacts:
       Emblem of Severed Fate Magnificent Tsuba:
       FIGHT_PROP_HP:4780.0
           FIGHT_PROP_HP_PERCENT:5.3
           FIGHT_PROP_ELEMENT_MASTERY:37.0
           FIGHT_PROP_CRITICAL_HURT:26.4
           FIGHT_PROP_CRITICAL:5.4
       Emblem of Severed Fate Sundered Feather:
       FIGHT_PROP_ATTACK:311.0
           FIGHT_PROP_HP_PERCENT:10.5
           FIGHT_PROP_CRITICAL:10.1
           FIGHT_PROP_CRITICAL_HURT:13.2
           FIGHT_PROP_CHARGE_EFFICIENCY:11.0
       Emblem of Severed Fate Storm Cage:
       FIGHT_PROP_CHARGE_EFFICIENCY:51.8
           FIGHT_PROP_CRITICAL:7.8
           FIGHT_PROP_CRITICAL_HURT:13.2
           FIGHT_PROP_HP_PERCENT:4.1
           FIGHT_PROP_HP:1105.0
       Emblem of Severed Fate Scarlet Vessel:
       FIGHT_PROP_HP_PERCENT:46.6
           FIGHT_PROP_CRITICAL:5.8
           FIGHT_PROP_CRITICAL_HURT:22.5
           FIGHT_PROP_CHARGE_EFFICIENCY:9.7
           FIGHT_PROP_DEFENSE_PERCENT:14.6
       Crimson Witch of Flames Witch's Scorching Hat:
       FIGHT_PROP_CRITICAL:31.1
           FIGHT_PROP_HP:478.0
           FIGHT_PROP_HP_PERCENT:10.5
           FIGHT_PROP_ATTACK:19.0
           FIGHT_PROP_CRITICAL_HURT:20.2
   Name: Kamisato Ayato
   Weapon: Haran Geppaku Futsu
   Artifacts:
       Heart of Depth Gilded Corsage:
       FIGHT_PROP_HP:4780.0
           FIGHT_PROP_CRITICAL_HURT:21.8
           FIGHT_PROP_HP_PERCENT:5.8
           FIGHT_PROP_CRITICAL:9.3
           FIGHT_PROP_ATTACK:14.0
       Ocean-Hued Clam Deep Palace's Plume:
       FIGHT_PROP_ATTACK:311.0
           FIGHT_PROP_ATTACK_PERCENT:5.3
           FIGHT_PROP_CRITICAL:10.5
           FIGHT_PROP_CRITICAL_HURT:21.8
           FIGHT_PROP_HP:299.0
       Heart of Depth Copper Compass:
       FIGHT_PROP_ATTACK_PERCENT:46.6
           FIGHT_PROP_HP:209.0
           FIGHT_PROP_HP_PERCENT:8.2
           FIGHT_PROP_CRITICAL:5.8
           FIGHT_PROP_CRITICAL_HURT:20.2
       Heart of Depth Goblet of Thundering Deep:
       FIGHT_PROP_WATER_ADD_HURT:46.6
           FIGHT_PROP_CRITICAL:6.6
           FIGHT_PROP_CRITICAL_HURT:26.4
           FIGHT_PROP_CHARGE_EFFICIENCY:5.2
           FIGHT_PROP_ATTACK_PERCENT:4.1
       Heart of Depth Wine-Stained Tricorne:
       FIGHT_PROP_CRITICAL_HURT:62.2
           FIGHT_PROP_CHARGE_EFFICIENCY:11.0
           FIGHT_PROP_ATTACK_PERCENT:9.3
           FIGHT_PROP_DEFENSE:35.0
           FIGHT_PROP_CRITICAL:6.6
......
```

If you want full docs for the API, visit [EnkaNetwork API](https://github.com/EnkaNetwork/API-docs)

# LICENSE
[MIT License](./LICENSE)