from MyTgBot import mongodb

usersdb = mongodb.users

async def is_served_user(user_id: int) -> bool:
    users = usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_served_users() -> list:
    users = usersdb.find({"user_id": {"$gt": 0}})
    if not users:
        return []
    users_list = []
    for user in await users.to_list(length=1000000000):
        users_list.append(user)
    return users_list


async def add_served_user(user_id: int):
    if is_served_user:
        return
    return await usersdb.insert_one({"user_id": user_id})
