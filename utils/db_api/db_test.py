import asyncio

from db_gino import db
from utils.db_api import quick_commands as commands

from data import config

from gino import Gino

db = Gino()

gino = Gino()


async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(1, 'Dan', 'net')
    await commands.add_user(14234, 'name', 'second name')
    await commands.add_user(134, 'fleymer', '234324')
    await commands.add_user(1343, 'vlad', '213')
    await commands.add_user(134342, 'bot', '12434')

    users = await commands.select_all_users()
    print(users)

    count = await commands.count_users()
    print(count)

    user = await commands.select_user()
    print(user)

    await commands.update_user_name(1 , 'New Vlad Name')
    print(user)

loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())
