import jwt
from settings.Settings import global_settings
from models.Authentication import Token


class JWT:
    @staticmethod
    def create():
        pass

    @staticmethod
    def validate(token) -> str:
        payload = jwt.decode(token, key=global_settings.JWT_TOKEN)
        payload = Token(**payload)
        return payload.user_id
