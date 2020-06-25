from settings.Settings import global_settings
from models.Tools import PaginationModel
from fastapi import HTTPException
import uuid
from random import randint


class Tools:
    PAGE_SIZE = global_settings.MAX_PAGE

    @staticmethod
    def pagination(page=1) -> PaginationModel:
        x = page - 1
        skip = Tools.PAGE_SIZE * x
        return PaginationModel(limit=Tools.PAGE_SIZE, skip=skip)

    @staticmethod
    def mongodb_id_converter(data: dict) -> dict:
        data["id"] = str(data["_id"])
        data.pop('_id')
        return data

    @staticmethod
    async def combine_two_list(list_one: list, list_two: list) -> list:
        return list(set(list_one + list_two))

    @staticmethod
    async def update_result_checker(result, message: str = 'nothing has been updated'):
        if result.modified_count == 0:
            raise HTTPException(detail=message, status_code=400)

    @staticmethod
    async def secret_key_generator():
        return str(uuid.uuid4())

    @staticmethod
    async def code_generator():
        return randint(1000, 9999)
