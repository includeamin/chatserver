from pydantic import BaseSettings


class Settings(BaseSettings):
    AUTH: bool = True
    JWT_TOKEN: str = 'simple_key'
    MAX_PAGE: int = 15


class DATABASE(BaseSettings):
    DATABASE_URL: str = 'mongodb://localhost:27017'
    DATABASE_NAME: str = 'chat_server'
    REDIS_URL: str = 'redis://'
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: str = 6379
    GROUPS_CHAT_COLLECTION: str = 'groups'
    DIRECT_CHAT_COLLECTION: str = 'directs'
    CHANNEL_CHAT_COLLECTION: str = 'channels'
    SIGNALING_COLLECTION: str = 'signaling'


class Bridges(BaseSettings):
    UserService: str = 'http://localhost:3002'
    GET_USER_INFO_URL: str = f'{UserService}/system/user/user_info'


class EventNames(BaseSettings):
    SERVER_RESPONSE: str = "server_response"
    DIRECT_MESSAGE: str = "direct_message"


class Permissions(BaseSettings):
    USER_CREATE_GROUP: bool = True


database_settings = DATABASE()
global_settings = Settings()
events_names = EventNames()
permissions_settings = Permissions()
bridge_settings = Bridges()
