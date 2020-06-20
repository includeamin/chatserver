from pydantic import BaseSettings


class Settings(BaseSettings):
    AUTH: bool = True
    JWT_TOKEN: str = 'simple_key'


class DATABASE(BaseSettings):
    DATABASE_URL: str = 'mongodb://localhost:27017'
    REDIS_URL: str = 'redis://'
    GROUPS_CHAT_COLLECTION: str = 'groups'
    DIRECT_CHAT_COLLECTION: str = 'directs'
    CHANNEL_CHAT_COLLECTION: str = 'channels'
    SIGNALING_COLLECTION: str = 'signaling'


database_settings = DATABASE()
global_settings = Settings()
