import pytest
import tests
from pathlib import Path

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from demo_qa.tests import attach


def resource_path(file_name):
    return str(
        Path(tests.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )


@pytest.fixture(scope='function')
def setup_browser():
    browser_version = "100.0"
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield browser

    # attach.add_screenshot(browser)
    # attach.add_html(browser)
    # attach.add_logs(browser)
    # attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope="function", autouse=True)
def browser_management(setup_browser):
    browser.config.base_url = "https://demoqa.com/"
    browser.config.timeout = 2.0
    browser.config.window_height = 2560
    browser.config.window_width = 1440
