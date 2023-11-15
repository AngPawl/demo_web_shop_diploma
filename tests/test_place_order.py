import allure
from allure_commons.types import Severity

from demo_web_shop_diploma.data import users
from demo_web_shop_diploma.data.search_queries import search_queries
from demo_web_shop_diploma.web_app import web_app


@allure.feature('Place order')
@allure.title(
    'Newly registered user without saved billing address successfully places an order'
)
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Place order')
@allure.severity(Severity.CRITICAL)
def test_newly_registered_user_without_billing_address_successfully_places_order():
    # Given
    user = users.create_customer_with_new_email()
    web_app.open()

    # When
    web_app.registration_page.register_user(user)

    web_app.search_page.search_for_query(search_queries.for_order_placing)
    web_app.item_card.add_product_to_cart()

    web_app.shopping_cart_page.open()
    web_app.shopping_cart_page.check_terms_of_service()
    web_app.checkout_page.go_to()

    web_app.checkout_page.go_through_checkout_process_without_billing_address(user)

    # Then
    web_app.order_completed_page.order_is_successfully_placed()


@allure.feature('Place order')
@allure.title(
    'Already registered user with a saved billing address successfully places an order'
)
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Place order')
@allure.severity(Severity.CRITICAL)
def test_user_with_billing_address_saved_successfully_places_order(login_through_api):
    # Given
    web_app.open()

    # When
    web_app.search_page.search_for_query(search_queries.for_order_placing)
    web_app.item_card.add_product_to_cart()

    web_app.shopping_cart_page.open()
    web_app.shopping_cart_page.check_terms_of_service()
    web_app.checkout_page.go_to()

    web_app.checkout_page.go_through_checkout_process_with_billing_address_already_saved()

    # Then
    web_app.order_completed_page.order_is_successfully_placed()
