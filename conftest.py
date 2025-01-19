import pytest
from services.dm_api.account.account import AccountApi
from services.dm_api.account.login import LoginApi
from services.mailhog.mailhog import MailhogApi
from configs.logger import setup_logging
from configs.configuration import Configuration

# Инициализация логгера при старте тестов
setup_logging()

@pytest.fixture
def config_data():
    """
    Конфигурация для API endpoints
    """
    return {
        'host': 'http://5.63.153.31:5051',
        'mailhog_host': 'http://5.63.153.31:5025'
    }

@pytest.fixture
def main_config(config_data):
    """
        disable_log:
            False - логирование запросов и ответов включено
            True - логирование запросов и ответов выключено
            По умолчанию установлено в True
     """
    return Configuration(
        host=config_data['host'],
        headers={
            'Content-Type': 'application/json'
        },
        disable_log=False
    )

@pytest.fixture
def mailhog_config(config_data):
    return Configuration(
        host=config_data['mailhog_host'],
        disable_log=True  # логи отключены для mailhog
    )

@pytest.fixture
def account(main_config):
    return AccountApi(configuration=main_config)

@pytest.fixture
def login(main_config):
    return LoginApi(configuration=main_config)

@pytest.fixture
def mailhog(mailhog_config):
    return MailhogApi(configuration=mailhog_config)