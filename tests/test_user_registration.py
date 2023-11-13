import allure
from allure_commons.types import Severity

from demo_web_shop_diploma.data import users
from demo_web_shop_diploma.web_app import web_app


@allure.title('User successfully registers')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Registration')
@allure.severity(Severity.CRITICAL)
def test_user_is_successfully_registered():
    web_app.open()

    web_app.registration_page.register_user(users.create_customer_with_new_email())

    web_app.registration_page.user_has_successfully_registered()


@allure.title('User is already registered')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Registration')
@allure.severity(Severity.CRITICAL)
def test_user_is_already_registered():
    web_app.open()

    web_app.registration_page.register_user(users.registered_customer)

    web_app.registration_page.user_validation_error_should_render()
