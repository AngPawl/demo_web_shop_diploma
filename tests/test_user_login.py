import copy

import allure
import pytest
from allure_commons.types import Severity

from demo_web_shop_diploma.data import users
from demo_web_shop_diploma.web_app import web_app


@allure.feature('Login')
@allure.title('User successfully logs in')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Login')
@allure.severity(Severity.CRITICAL)
def test_user_successfully_logs_in():
    web_app.open()

    web_app.login_page.log_in(users.registered_customer)

    web_app.login_page.user_has_successfully_logged_in(users.registered_customer)


@allure.feature('Login')
@allure.title('User cannot log in without being registered')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Login')
@allure.severity(Severity.CRITICAL)
def test_unregistered_user_cannot_log_in():
    web_app.open()

    web_app.login_page.log_in(users.create_customer_with_new_email())

    web_app.login_page.no_account_error_renders()


@allure.feature('Login')
@allure.title('User cannot log in with invalid password')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Login')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize('invalid_password', ['.', '12345', ' '])
def test_registered_user_cannot_log_in_with_invalid_password(invalid_password):
    user = copy.copy(users.registered_customer)
    user.password = invalid_password
    web_app.open()

    web_app.login_page.log_in(user)

    web_app.login_page.invalid_credentials_error_renders()
