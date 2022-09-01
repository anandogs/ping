import logging
import os
from pydantic import BaseSettings, AnyUrl
from functools import lru_cache


log = logging.getLogger('uvicorn')

class Settings(BaseSettings):
    environment:str = os.environ.get('ENVIRONMENT', 'dev')
    testing:bool = os.environ.get('TESTING', 0)
    database_url:AnyUrl = os.environ.get('DATABASE_URL')

@lru_cache()
def get_settings() -> BaseSettings:
    log.info('Loading config settings from the environment')
    return Settings()