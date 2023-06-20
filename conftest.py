import pytest
from selene.support.shared import browser, config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from session.session import BaseSession
from utils import attach
from steps.api_steps import ApiSteps


@pytest.fixture
def set_config_browser():
    config.window_width = '1920'
    config.window_height = '1080'
    config.base_url = 'https://kz.siberianwellness.com/kz-ru/'

    option = Options()

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    option.capabilities.update(capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=option)
    config.driver = driver

    yield
    attach.add_video(browser)
    attach.add_screenshot(browser)

    browser.quit()


@pytest.fixture
def set_debug_config():
    config.window_width = '1920'
    config.window_height = '1080'
    config.base_url = 'https://kz.siberianwellness.com/kz-ru/'
    yield
    browser.quit()


@pytest.fixture
def get_base_url():
    return "https://kz.siberianwellness.com/api/v1/"


@pytest.fixture
def get_session(get_base_url):
    return BaseSession(base_url=get_base_url)


@pytest.fixture
def get_api_step(get_session):
    step = ApiSteps()
    step.api_session = get_session
    step.api_session.headers['token'] = step.api_session.get('myValidToken').json()['Model']['Token']

    return step
