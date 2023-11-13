import allure
from selene import browser


class ShoppingCartPage:
    @allure.step('Open Shopping Cart Page')
    def open(self):
        browser.element('.ico-cart').click()

    @allure.step('Check Terms of Service')
    def check_terms_of_service(self):
        browser.element('#termsofservice').click()
