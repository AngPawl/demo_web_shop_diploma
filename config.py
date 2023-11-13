from typing import Literal

from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class Config(BaseSettings):
    login: str
    password: str
    browser_url: str
    context: Literal['local', 'remote'] = 'local'
    browser_name: Literal['chrome', 'firefox'] = 'chrome'
    base_url: str = "https://demowebshop.tricentis.com/"
    window_width: int = 1366
    window_height: int = 768
    headless: bool = False


load_dotenv()
config = Config()
