import jwt
from settings.Settings import global_settings, bridge_settings
from models.Authentication import Token
from fastapi import HTTPException, Header
from py_cas.CAS import CAS
from py_cas.Models import *

conf = InitConfig(service_address=bridge_settings.CAS_SERVICE)
cas_client = CAS(conf=conf)


class JWT:
    @staticmethod
    def create():
        pass

    @staticmethod
    def validate(token) -> str:
        # payload = jwt.decode(token, key=global_settings.JWT_TOKEN)
        # payload = Token(**payload)
        # return payload.user_id
        return token


class TokenValidation:
    def __init__(self, permission: str = None):
        self.permission = permission

    def __call__(self, token: str = Header(None)):
        if not token:
            raise HTTPException(detail="token required", status_code=400)
        try:
            if self.permission:
                result = cas_client.validate_token(token=token, permission=self.permission)
            else:
                # result = JWT.validate(token)
                result = token

        except Exception as ex:
            raise HTTPException(detail=ex.args[0], status_code=400)
        # return ObjectId(result.user_id)
        return result.user_id
