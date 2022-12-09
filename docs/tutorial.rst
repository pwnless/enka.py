Tutorial
========
enka.py allows you to fetch genshin user data easily.

**Note: ALL operation is async**

Fetching genshin user data
--------------------------
For now, enka.network has only one public API, which fetches all data via genshin uid.

*Note: all data are same as what you see in game.*

Example::

    from enkapy import Enka
    import asyncio
    client = Enka()

    async def main():
        await client.load_lang()
        user = await client.fetch_user(104267816)
        print(user)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

.. code-block::py

User data object
-----------------

What you get in previous step are :py:class:`enkapy.model.EnkaData` object

It contains all information about the specific player.

There are 2 main data fields in this object:

* characters: ALL characters data the player choose to shown in game
* player: Basic information about this player

Loading language data
----------------------

So you might already noticed, why ``await client.load_lang``?

Because name related data aren't in the data returned from enka.network, we need to parse the name from some integer.

The process is roughly looking up int value in genshin related json file, and somehow grab a name hash and look it up
in genshin TextMap json file.

We automated this process, just pass the correct language value(default 'en') and call :py:func:`enkapy.client.Enka.load_lang`

*New in 1.1.0: Now load_lang has cache! check ``force_cache`` and ``force_update`` parameters!*

*Note: if you don't load language data, all name field in returned object will be empty string*

Player basic info
------------------
Example::

    await client.load_lang()
    user = await client.fetch_user(104267816)
    print(f"Nickname: {user.player.nickname}")
    print(f"Level: {user.player.level}")
    print(f'Signature: {user.player.signature}')
    print(f'World level:{user.player.worldLevel}')
    print(f'Abyss: {user.player.towerFloorIndex}-{user.player.towerLevelIndex}')

.. code-block::py

Result::

    Nickname: 天天向上
    Level: 60
    Signature: 凌人有点无脑
    World level:8
    Abyss: 12-3

.. code-block::text

Character info
---------------
*Note: you might not able to fetch this info if player choose not to share*

Basically there are 5 parts of character info:

* character basic info(name/friendship/ascension...etc)
* character weapon info
* character constellations info
* character artifact info
* character skill info

Character basic info::

    character = user.characters[0]
    print(f'Name: {character.name}')
    print(f'Ascension: {character.ascension}')
    print(f'Level: {character.level}')
    print(f'Exp: {character.experience}')

.. code-block::py

Character weapon info::

    print('Weapon:')
    weapon = character.weapon
    print(f'\tName: {weapon.name}')
    print(f'\tLevel: {weapon.level}')
    print(f'\tRefine: {weapon.refine}')
    print(f'\tStar level: {weapon.rank}')

.. code-block::py

Character constellations info::

    print('Constellations:')
    for constellation in character.constellations:
        if constellation.activated:
            print(f'\t{constellation.name} Activated')

.. code-block::py

Character artifact info::

    print('Artifacts:')
    for artifact in character.artifacts:
        print(f'\t{artifact.set_name} {artifact.name}:')
        print(f'\t{artifact.main_stat.prop}:{artifact.main_stat.value}')
        for sub_stats in artifact.sub_stats:
            print(f'\t\t{sub_stats.prop}:{sub_stats.value}')

.. code-block::py

Character skill info::

    print('Skills:')
    for skill in character.skills:
        if skill.type == 0:
            print(f'\tNormal skill {skill.name}, level:{skill.level}')
        elif skill.type == 1:
            print(f'\tElemental skill {skill.name}, level:{skill.level}')
        elif skill.type == 2:
            print(f'\tElemental burst {skill.name}, level:{skill.level}')

.. code-block::py