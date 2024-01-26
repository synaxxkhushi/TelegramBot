from MyTgBot import mongodb

db = mongodb.USERS

self.usersdb = self.db.usersdb

    def get_users(self) -> list:
        user = self.usersdb.find()
        if not user:
            return []
        user_list = []
        for user in await user.to_list(length=1000000000):
            user_list.append(int(user["user_id"]))
        return user_list

    def is_user(self, user_id: int) -> bool:
        user = await self.usersdb.find_one({"user_id": user_id})
        if not user:
            return False
        return True

    def add_user(self, user_id: int):
        is_served = await self.is_user(user_id)
        if is_served:
            return
        return await self.usersdb.insert_one({"user_id": user_id})
