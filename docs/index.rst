.. enka.py documentation master file, created by
   sphinx-quickstart on Thu Jun 30 20:07:43 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to enka.py's documentation!
===================================
enka.py is a friendly API wrapper for https://enka.shinshin.moe/

https://enka.shinshin.moe/ is a awesome website for fetching genshin impact user data

Install
-------
.. code-block:: sh

   pip3 install enka.py

Example
-------
.. code-block:: python

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

Output

.. code-block::

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
   Name: Eula
   Weapon: Song of Broken Pines
   Artifacts:
       Pale Flame Stainless Bloom:
       FIGHT_PROP_HP:4780.0
           FIGHT_PROP_CRITICAL_HURT:5.4
           FIGHT_PROP_CRITICAL:14.8
           FIGHT_PROP_ATTACK_PERCENT:4.1
           FIGHT_PROP_ATTACK:29.0
       Bloodstained Chivalry Bloodstained Black Plume:
       FIGHT_PROP_ATTACK:311.0
           FIGHT_PROP_ELEMENT_MASTERY:16.0
           FIGHT_PROP_DEFENSE:21.0
           FIGHT_PROP_CRITICAL_HURT:26.4
           FIGHT_PROP_CRITICAL:7.0
       Bloodstained Chivalry Bloodstained Final Hour:
       FIGHT_PROP_ATTACK_PERCENT:46.6
           FIGHT_PROP_CRITICAL:10.9
           FIGHT_PROP_CHARGE_EFFICIENCY:15.5
           FIGHT_PROP_DEFENSE:19.0
           FIGHT_PROP_CRITICAL_HURT:7.8
       Lavawalker Lavawalker's Epiphany:
       FIGHT_PROP_PHYSICAL_ADD_HURT:58.3
           FIGHT_PROP_CRITICAL_HURT:13.2
           FIGHT_PROP_CRITICAL:14.0
           FIGHT_PROP_ATTACK_PERCENT:4.1
           FIGHT_PROP_ELEMENT_MASTERY:19.0
       Pale Flame Mocking Mask:
       FIGHT_PROP_CRITICAL:31.1
           FIGHT_PROP_HP:508.0
           FIGHT_PROP_ELEMENT_MASTERY:40.0
           FIGHT_PROP_ATTACK_PERCENT:14.6
           FIGHT_PROP_CRITICAL_HURT:6.2
   Name: Shenhe
   Weapon: Calamity Queller
   Artifacts:
       Gladiator's Finale Gladiator's Nostalgia:
       FIGHT_PROP_HP:4780.0
           FIGHT_PROP_CHARGE_EFFICIENCY:14.9
           FIGHT_PROP_CRITICAL_HURT:7.8
           FIGHT_PROP_CRITICAL:7.8
           FIGHT_PROP_ATTACK_PERCENT:17.5
       Shimenawa's Reminiscence Shaft of Remembrance:
       FIGHT_PROP_ATTACK:311.0
           FIGHT_PROP_CRITICAL:3.1
           FIGHT_PROP_ATTACK_PERCENT:5.3
           FIGHT_PROP_CRITICAL_HURT:29.5
           FIGHT_PROP_CHARGE_EFFICIENCY:10.4
       Noblesse Oblige Royal Pocket Watch:
       FIGHT_PROP_ATTACK_PERCENT:46.6
           FIGHT_PROP_ELEMENT_MASTERY:21.0
           FIGHT_PROP_CRITICAL:6.6
           FIGHT_PROP_ATTACK:16.0
           FIGHT_PROP_CHARGE_EFFICIENCY:23.3
       Gladiator's Finale Gladiator's Intoxication:
       FIGHT_PROP_ATTACK_PERCENT:46.6
           FIGHT_PROP_HP:508.0
           FIGHT_PROP_CRITICAL_HURT:28.0
           FIGHT_PROP_CRITICAL:3.9
           FIGHT_PROP_CHARGE_EFFICIENCY:11.0
       Shimenawa's Reminiscence Capricious Visage:
       FIGHT_PROP_ATTACK_PERCENT:46.6
           FIGHT_PROP_ELEMENT_MASTERY:44.0
           FIGHT_PROP_CRITICAL:5.8
           FIGHT_PROP_CRITICAL_HURT:22.5
           FIGHT_PROP_ATTACK:18.0
   Name: Raiden Shogun
   Weapon: Engulfing Lightning
   Artifacts:
       Emblem of Severed Fate Magnificent Tsuba:
       FIGHT_PROP_HP:4780.0
           FIGHT_PROP_CRITICAL:17.5
           FIGHT_PROP_ELEMENT_MASTERY:19.0
           FIGHT_PROP_CRITICAL_HURT:6.2
           FIGHT_PROP_DEFENSE_PERCENT:5.8
       Emblem of Severed Fate Sundered Feather:
       FIGHT_PROP_ATTACK:311.0
           FIGHT_PROP_CHARGE_EFFICIENCY:13.0
           FIGHT_PROP_CRITICAL:6.2
           FIGHT_PROP_DEFENSE_PERCENT:7.3
           FIGHT_PROP_CRITICAL_HURT:25.6
       Emblem of Severed Fate Storm Cage:
       FIGHT_PROP_CHARGE_EFFICIENCY:51.8
           FIGHT_PROP_CRITICAL_HURT:18.7
           FIGHT_PROP_ATTACK:18.0
           FIGHT_PROP_CRITICAL:7.4
           FIGHT_PROP_DEFENSE:35.0
       Gladiator's Finale Gladiator's Intoxication:
       FIGHT_PROP_ELEC_ADD_HURT:46.6
           FIGHT_PROP_CRITICAL_HURT:16.3
           FIGHT_PROP_CHARGE_EFFICIENCY:11.7
           FIGHT_PROP_CRITICAL:5.4
           FIGHT_PROP_DEFENSE_PERCENT:7.3
       Emblem of Severed Fate Ornate Kabuto:
       FIGHT_PROP_CRITICAL:31.1
           FIGHT_PROP_DEFENSE_PERCENT:7.3
           FIGHT_PROP_ATTACK_PERCENT:17.5
           FIGHT_PROP_CHARGE_EFFICIENCY:10.4
           FIGHT_PROP_CRITICAL_HURT:14.8
   Name: Kaedehara Kazuha
   Weapon: Freedom-Sworn
   Artifacts:
       Viridescent Venerer In Remembrance of Viridescent Fields:
       FIGHT_PROP_HP:4780.0
           FIGHT_PROP_ELEMENT_MASTERY:40.0
           FIGHT_PROP_CRITICAL:7.0
           FIGHT_PROP_ATTACK:14.0
           FIGHT_PROP_CRITICAL_HURT:17.9
       Viridescent Venerer Viridescent Arrow Feather:
       FIGHT_PROP_ATTACK:311.0
           FIGHT_PROP_DEFENSE:39.0
           FIGHT_PROP_CRITICAL_HURT:10.9
           FIGHT_PROP_ELEMENT_MASTERY:63.0
           FIGHT_PROP_HP:538.0
       Viridescent Venerer Viridescent Venerer's Determination:
       FIGHT_PROP_ELEMENT_MASTERY:187.0
           FIGHT_PROP_CHARGE_EFFICIENCY:5.8
           FIGHT_PROP_ATTACK_PERCENT:15.7
           FIGHT_PROP_HP:598.0
           FIGHT_PROP_DEFENSE:39.0
       Viridescent Venerer Viridescent Venerer's Vessel:
       FIGHT_PROP_ELEMENT_MASTERY:187.0
           FIGHT_PROP_ATTACK_PERCENT:4.1
           FIGHT_PROP_CRITICAL_HURT:18.7
           FIGHT_PROP_HP:299.0
           FIGHT_PROP_DEFENSE:63.0
       Wanderer's Troupe Conductor's Top Hat:
       FIGHT_PROP_ELEMENT_MASTERY:187.0
           FIGHT_PROP_CRITICAL:8.2
           FIGHT_PROP_ATTACK:14.0
           FIGHT_PROP_CHARGE_EFFICIENCY:6.5
           FIGHT_PROP_CRITICAL_HURT:21.0
   Name: Yae Miko
   Weapon: Kagura's Verity
   Artifacts:
       Gladiator's Finale Gladiator's Nostalgia:
       FIGHT_PROP_HP:4780.0
           FIGHT_PROP_CRITICAL:7.8
           FIGHT_PROP_HP_PERCENT:11.1
           FIGHT_PROP_ELEMENT_MASTERY:35.0
           FIGHT_PROP_CRITICAL_HURT:20.2
       Thundering Fury Survivor of Catastrophe:
       FIGHT_PROP_ATTACK:311.0
           FIGHT_PROP_DEFENSE:37.0
           FIGHT_PROP_CRITICAL:7.4
           FIGHT_PROP_HP:478.0
           FIGHT_PROP_CRITICAL_HURT:18.7
       Thundering Fury Hourglass of Thunder:
       FIGHT_PROP_ATTACK_PERCENT:46.6
           FIGHT_PROP_ATTACK:33.0
           FIGHT_PROP_HP:568.0
           FIGHT_PROP_CRITICAL_HURT:21.8
           FIGHT_PROP_ELEMENT_MASTERY:19.0
       Wanderer's Troupe Wanderer's String-Kettle:
       FIGHT_PROP_ELEC_ADD_HURT:46.6
           FIGHT_PROP_ATTACK:19.0
           FIGHT_PROP_CRITICAL_HURT:28.8
           FIGHT_PROP_HP:777.0
           FIGHT_PROP_CRITICAL:3.9
       Gladiator's Finale Gladiator's Triumphus:
       FIGHT_PROP_CRITICAL:31.1
           FIGHT_PROP_ELEMENT_MASTERY:33.0
           FIGHT_PROP_ATTACK_PERCENT:8.7
           FIGHT_PROP_ATTACK:37.0
           FIGHT_PROP_CRITICAL_HURT:12.4


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Github<https://github.com/pwnblog/enka.py>
   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
