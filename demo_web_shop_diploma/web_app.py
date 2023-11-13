import allure
from selene import browser

from demo_web_shop_diploma.components.item_card import ItemCard
from demo_web_shop_diploma.pages.checkout_page import CheckoutPage
from demo_web_shop_diploma.pages.login_page import LoginPage
from demo_web_shop_diploma.pages.order_completed_page import OrderCompletedPage
from demo_web_shop_diploma.pages.registration_page import RegistrationPage
from demo_web_shop_diploma.pages.search_page import SearchPage
from demo_web_shop_diploma.pages.shopping_cart_page import ShoppingCartPage


class WebApp:
    def __init__(self):
        self.item_card = ItemCard()
        self.checkout_page = CheckoutPage()
        self.order_completed_page = OrderCompletedPage()
        self.registration_page = RegistrationPage()
        self.login_page = LoginPage()
        self.search_page = SearchPage()
        self.shopping_cart_page = ShoppingCartPage()

    @staticmethod
    @allure.step('Open web app')
    def open():
        browser.open('')


web_app = WebApp()
