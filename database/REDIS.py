from redis import Redis
from settings.Settings import database_settings

redis_db = Redis(host=database_settings.REDIS_HOST, port=database_settings.REDIS_PORT)