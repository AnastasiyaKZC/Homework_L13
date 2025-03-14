import pytest
from selene import browser
from utils import attach

@pytest.fixture(scope="function", autouse=True)
def browser_managment():
    browser.config.window_width = 1280
    browser.config.window_height = 1220
    # browser.config.base_url = "https://demoqa.com/automation-practice-form"
    browser.config.timeout = 2.0

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser) # консольные ошибки браузера
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()