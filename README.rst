.. _enkapy:

Enka.py
=======

Friendly API for fetching genshin user data from
`https://enka.shinshin.moe/ <https://enka.shinshin.moe/>`__

Added name parsing and full artifact support and more elegant code.

original from
`https://github.com/mrwan200/EnkaNetwork.py <https://github.com/mrwan200/EnkaNetwork.py>`__

Installation
============

::

   pip install enka.py

Usage
=====

.. code:: py

   import asyncio

   from enkapy import Enka

   client = Enka()


   async def main():
       await client.load_lang() # load the lang data from remote repo, otherwise all names will be null string.
       user = await client.fetch_user(700378769)
       print(f"Nickname: {user.player.nickname}")
       print(f"Level: {user.player.level}")
       for character in user.characters:
           print(f'Name: {character.name}')
           print(f'Weapon: {character.weapon.flat.nameText}')
           print('Artifacts:')
           for artifact in character.artifacts:
               print(f'\t{artifact.flat.setNameText} {artifact.flat.nameText}:')
               print(f'\t{artifact.flat.main_stat.prop}:{artifact.flat.main_stat.value}')
               for sub_stats in artifact.flat.sub_stats:
                   print(f'\t\t{sub_stats.prop}:{sub_stats.value}')


   loop = asyncio.get_event_loop()
   loop.run_until_complete(main())

.. code:: sh

   Nickname: ExLin
   Level: 59
   Name: Yoimiya
   Weapon: Rust
   Artifacts:
       Noblesse Oblige Royal Flora:
       FIGHT_PROP_HP:4780
           FIGHT_PROP_CRITICAL:11
           FIGHT_PROP_CRITICAL_HURT:14
           FIGHT_PROP_ATTACK:19
           FIGHT_PROP_ATTACK_PERCENT:10
       Noblesse Oblige Royal Plume:
       FIGHT_PROP_ATTACK:311
           FIGHT_PROP_CRITICAL:14
           FIGHT_PROP_ELEMENT_MASTERY:42
           FIGHT_PROP_HP_PERCENT:5
           FIGHT_PROP_ATTACK_PERCENT:5
       Lavawalker Lavawalker's Torment:
       FIGHT_PROP_ATTACK_PERCENT:46
           FIGHT_PROP_CHARGE_EFFICIENCY:5
           FIGHT_PROP_HP:568
           FIGHT_PROP_CRITICAL:8
           FIGHT_PROP_CRITICAL_HURT:12
       Gladiator's Finale Gladiator's Intoxication:
       FIGHT_PROP_FIRE_ADD_HURT:46
           FIGHT_PROP_ATTACK:37
           FIGHT_PROP_ATTACK_PERCENT:15
           FIGHT_PROP_CRITICAL_HURT:14
           FIGHT_PROP_CRITICAL:7
       Noblesse Oblige Royal Masque:
       FIGHT_PROP_CRITICAL_HURT:62
           FIGHT_PROP_CRITICAL:9
           FIGHT_PROP_ATTACK:19
           FIGHT_PROP_ATTACK_PERCENT:5
           FIGHT_PROP_HP:747
   Name: Albedo
   Weapon: Cinnabar Spindle
   Artifacts:
       Husk of Opulent Dreams Calabash of Awakening:
       FIGHT_PROP_ROCK_ADD_HURT:46
           FIGHT_PROP_CRITICAL_HURT:7
           FIGHT_PROP_ELEMENT_MASTERY:40
           FIGHT_PROP_HP:508
           FIGHT_PROP_CRITICAL:10
   Name: Xiao
   Weapon: Lithic Spear
   Artifacts:
       Wanderer's Troupe Troupe's Dawnlight:
       FIGHT_PROP_HP:3967
           FIGHT_PROP_CRITICAL:5
           FIGHT_PROP_CHARGE_EFFICIENCY:9
           FIGHT_PROP_ELEMENT_MASTERY:44
           FIGHT_PROP_ATTACK_PERCENT:5
       Shimenawa's Reminiscence Shaft of Remembrance:
       FIGHT_PROP_ATTACK:232
           FIGHT_PROP_CHARGE_EFFICIENCY:6
           FIGHT_PROP_CRITICAL:5
           FIGHT_PROP_ATTACK_PERCENT:9
           FIGHT_PROP_HP_PERCENT:4
       Shimenawa's Reminiscence Morning Dew's Moment:
       FIGHT_PROP_ATTACK_PERCENT:14
           FIGHT_PROP_ATTACK:18
           FIGHT_PROP_CHARGE_EFFICIENCY:6
           FIGHT_PROP_CRITICAL_HURT:6
           FIGHT_PROP_ELEMENT_MASTERY:21
       Wanderer's Troupe Wanderer's String-Kettle:
       FIGHT_PROP_WIND_ADD_HURT:46
           FIGHT_PROP_ATTACK:14
           FIGHT_PROP_ATTACK_PERCENT:9
           FIGHT_PROP_CRITICAL:2
           FIGHT_PROP_CRITICAL_HURT:24
       Vermillion Hereafter Thundering Poise:
       FIGHT_PROP_CRITICAL:4
           FIGHT_PROP_HP:269
           FIGHT_PROP_CHARGE_EFFICIENCY:4
           FIGHT_PROP_ATTACK_PERCENT:4
           FIGHT_PROP_ATTACK:18
   ......

If you want full docs for the API, visit `EnkaNetwork
API <https://github.com/EnkaNetwork/API-docs>`__

LICENSE
=======

`MIT License <./LICENSE>`__
