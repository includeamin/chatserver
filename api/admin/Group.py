from models.Chat import *
from classes.Group import Group
from fastapi import APIRouter, Depends
from authentication.JWT import TokenValidation

admin_group_routes = APIRouter()


@admin_group_routes.post("/new", description="create new group", response_model=AdminCreateGroupResponseModel)
async def create_new_group(data: AdminCreateGroupBodyModel, user_id: Depends(TokenValidation())):
    result = await Group.Admin.create_group(data, user_id=user_id)
    return result


@admin_group_routes.put("/subscribe/{action}", description="subscribe user to group. add,remove")
async def subscribe_user(action: str, data: AdminSubscribeBodyModel):
    if action not in ['add', 'remove']:
        raise HTTPException(detail='invalid action, add or remove are valid', status_code=400)
    result = await Group.Admin.subscribe(gp_id=data.group_id, user_id=data.user_id, user_name=data.user_name,
                                         action=action)
    return result


@admin_group_routes.get("/subscribes", description="get subscribe og group")
async def get_subscribe_of_group(gp_name: str, page: int = 1):
    pass


@admin_group_routes.get("/groups", description="get list of groups")
async def get_groups():
    pass
