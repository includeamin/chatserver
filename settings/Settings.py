from pydantic import BaseSettings


class Settings(BaseSettings):
    AUTH: bool = True
    JWT_TOKEN: str = 'simple_key'


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


class EventNames(BaseSettings):
    SERVER_RESPONSE: str = "SERVER_RESPONSE"
    DIRECT_MESSAGE: str = "DIRECT_MESSAGE"


class Permissions(BaseSettings):
    USER_CREATE_GROUP: bool = True


database_settings = DATABASE()
global_settings = Settings()
events_names = EventNames()
permissions_settings = Permissions()
