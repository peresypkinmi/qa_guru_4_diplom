from selene.support.shared import browser, config
import pytest
from time import sleep
from utils import attach

from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser, config
from selenium import webdriver



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
