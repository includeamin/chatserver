import requests
from models.Bridge import PersonalInfo
from fastapi import HTTPException
from settings.Settings import bridge_settings


def get_user_information(user_id: str) -> PersonalInfo:
    result = requests.get(bridge_settings.GET_USER_INFO_URL, params={"user_id": user_id})
    if result.status_code != 200:
        raise HTTPException(detail=f"bridge failed to request {result.content}", status_code=result.status_code)
    data = PersonalInfo(**result.json())
    return data
