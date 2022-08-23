import logging
import os
from pydantic import BaseSettings
from functools import lru_cache


log = logging.getLogger('uvicorn')

class Settings(BaseSettings):
    environment:str = os.environ.get('ENVIRONMENT', 'dev')
    testing:bool = os.environ.get('TESTING', 0)

@lru_cache()
def get_settings() -> BaseSettings:
    log.info('Loading config settings from the environment')
    return Settings()