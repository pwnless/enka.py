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
