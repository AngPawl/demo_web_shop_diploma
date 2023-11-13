import allure
from selene import browser, have, be


class OrderCompletedPage:
    @allure.step('Page title should have correct text')
    def _page_title_should_have_correct_text(self):
        browser.element('.checkout-page .page-title h1').should(
            have.exact_text('Thank you')
        )

    @allure.step('Order completed section title should have correct text')
    def _order_completed_section_title_should_have_correct_text(self):
        browser.element('.order-completed .title').should(
            have.exact_text('Your order has been successfully processed!')
        )

    @allure.step('Order completed section info should contain order number')
    def _order_completed_section_info_should_contain_order_number(self):
        browser.element('.order-completed .details').should(have.text('Order number: '))

    @allure.step('Order completed Continue button should render')
    def _order_completed_continue_button_should_render(self):
        browser.element('.order-completed-continue-button').should(be.clickable)

    @allure.step('Order is successfully placed')
    def order_is_successfully_placed(self):
        self._page_title_should_have_correct_text()
        self._order_completed_section_title_should_have_correct_text()
        self._order_completed_section_info_should_contain_order_number()
        self._order_completed_continue_button_should_render()
