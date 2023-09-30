"""фикстуры используемые для тестирования формы
https://demoqa.com/automation-practice-form"""
import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def browser_setup():
    """Фикстура настройки браузера"""
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 2.0
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'


@pytest.fixture(scope='function')
def open_url(browser_setup):
    """Фикстура открытия браузера с указанным url"""
    browser.open('/')
    yield browser
    browser.quit()
