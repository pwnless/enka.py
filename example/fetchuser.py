import asyncio

from enkapy import Enka

client = Enka()


async def main():
    await client.load_lang()
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
            print(f'\ticon: {artifact.flat.icon_url}')
            for sub_stats in artifact.flat.sub_stats:
                print(f'\t\t{sub_stats.prop}:{sub_stats.value}')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
