import allure
import pytest
import requests
from selene import browser
from selenium import webdriver

from demo_web_shop_diploma.data import users
from demo_web_shop_diploma.utils import attach
from config import config


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    if config.browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        browser_version = '100'
    else:
        options = webdriver.FirefoxOptions()
        browser_version = '98'

    if config.context == 'remote':
        selenoid_capabilities = {
            "browserName": config.browser_name,
            "browserVersion": browser_version,
            "selenoid:options": {"enableVNC": True, "enableVideo": True},
        }
        options.capabilities.update(selenoid_capabilities)

        login = config.login
        password = config.password
        browser_url = config.browser_url

        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@{browser_url}",
            options=options,
        )

        browser.config.driver = driver

    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.driver_options = options
    browser.config.base_url = config.base_url

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)

    if config.browser_name == 'chrome':
        attach.add_logs(browser)

    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function', autouse=False)
def login_through_api():
    api_url = config.base_url

    url = api_url + "/login"
    auth_cookie_name = "NOPCOMMERCE.AUTH"
    payload = {
        'Email': users.registered_customer.email,
        "Password": users.registered_customer.password,
        "RememberMe": False,
    }
    response = requests.request("POST", url, data=payload, allow_redirects=False)
    cookie = response.cookies.get(auth_cookie_name)

    browser.open('')
    with allure.step('Authenticate user'):
        browser.driver.add_cookie({"name": auth_cookie_name, "value": cookie})
