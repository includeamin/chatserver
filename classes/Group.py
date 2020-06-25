from bson import ObjectId
from database.MONGO import group_chat_collection
from fastapi import HTTPException
from models.Chat import GroupDatabaseModel, AdminCreateGroupResponseModel, AdminCreateGroupBodyModel, CreateForModel, \
    SubscribeModel, GetUserSubscribes
from utils.Tools import Tools
from models.GlobalModel import GlobalResult


class Group:
    class Public:
        pass

    class Admin:
        @staticmethod
        async def create_group(data: AdminCreateGroupBodyModel, user_id: str) -> AdminCreateGroupResponseModel:
            result = await Group.Shared.create_group(data.name, user_id=user_id, create_by="admin",
                                                     create_for=data.create_for)
            return AdminCreateGroupResponseModel(group_id=result)

        @staticmethod
        async def subscribe(gp_id: str, user_id: str, user_name: str, action: str):
            await Group.Shared.subscribe(gp_id, user_id, user_name, action)
            return GlobalResult(message='done')

    class Shared:
        @staticmethod
        async def create_group(group_name: str, user_id: str = None,
                               create_by: str = None, create_for: CreateForModel = None) -> str:
            await Group.Shared.same(group_name, user_id)
            group = group_chat_collection.insert_one(
                GroupDatabaseModel(name=group_name, owner=user_id, create_by=create_by, create_for=create_for).dict())
            return str(group.inserted_id)

        @staticmethod
        async def same(group_name: str, owner: str):
            same = group_chat_collection.find_one({"name": group_name, 'owner': owner}, {})
            if same:
                raise HTTPException(detail="you have already group with this name", status_code=400)

        @staticmethod
        async def group_id_exist(_id: str):
            group = group_chat_collection.find_one({"_id": ObjectId(_id)}, {})
            if not group:
                raise HTTPException(detail="group not exist", status_code=404)

        @staticmethod
        async def subscribe(gp_id: str, user_id: str, user_name: str, action: str = 'add'):
            # await Group.Shared.group_id_exist(gp_id)
            result = group_chat_collection.update_one({"_id": ObjectId(gp_id)},
                                                      {"$addToSet" if action == 'add' else '$pull': {
                                                          'subscribes': SubscribeModel(user_id=user_id,
                                                                                       user_name=user_name).dict()
                                                      }})
            await Tools.update_result_checker(result)

        @staticmethod
        async def get_users_subscribes(user_id: str) -> GetUserSubscribes:
            pipeline = [{"$match": {"subscribes.user_id": user_id}},
                        {"$group": {
                            "_id": {"$toString": "$_id"}

                        }}]
            data = group_chat_collection.aggregate(pipeline=pipeline)
            gp_ids = [None]
            for item in data:
                gp_ids.append(item["_id"])

            return GetUserSubscribes(group_id=gp_ids)

        class System:

            @staticmethod
            async def create_group():
                pass
