from models.Chat import *
from classes.Group import Group
from fastapi import APIRouter

admin_group_routes = APIRouter()


@admin_group_routes.get("/new", description="create new group")
async def create_new_group(group_name: str):
    pass


@admin_group_routes.put("/subscribe/{action}", description="subscribe user to group. add,remove")
async def subscribe_user(action: str, group_id: str, user_id: str, user_name: str):
    pass


@admin_group_routes.get("/subscribes", description="get subscribe og group")
async def get_subscribe_of_group(gp_name: str, page: int = 1):
    pass


@admin_group_routes.get("/groups", description="get list of groups")
async def get_groups():
    pass
