from pydantic import BaseSettings


class Settings(BaseSettings):
    AUTH: bool = True
    AUTH_SERVER_URL: str = 'http://auth'


class DATABASE(BaseSettings):
    DATABASE_URL: str = 'mongodb://localhost:27017'
    REDIS_URL: str = ''
    GROUPS_CHAT_COLLECTION: str = 'groups'
    DIRECT_CHAT_COLLECTION: str = 'directs'
    CHANNEL_CHAT_COLLECTION: str = 'channels'
    SIGNALING_COLLECTION: str = 'signaling'


database_settings = DATABASE()
