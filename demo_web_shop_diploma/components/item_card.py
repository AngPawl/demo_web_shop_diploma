import allure
from selene import browser, have


class ItemCard:

    @allure.step('Add product to the cart')
    def add_product_to_cart(self):
        browser.element('[class~="product-box-add-to-cart-button"]').click()
        browser.element('#bar-notification .content').should(
            have.text('The product has been added to your shopping cart')
        )
        browser.element('.close').click()
