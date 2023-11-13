import allure
from selene import browser, have


class CheckoutPage:
    @allure.step('Go to Checkout page')
    def go_to(self):
        browser.element('#checkout').click()

    @allure.step('Select country: {country}')
    def _select_country(self, country):
        browser.all('#BillingNewAddress_CountryId option').element_by(
            have.exact_text(country)
        ).click()

    @allure.step('Fill in city: {city}')
    def _fill_in_city(self, city):
        browser.element('#BillingNewAddress_City').send_keys(city)

    @allure.step('Fill in address1: {address1}')
    def _fill_in_address1(self, address1):
        browser.element('#BillingNewAddress_Address1').send_keys(address1)

    @allure.step('Fill in zipcode: {zipcode}')
    def _fill_in_zipcode(self, zipcode):
        browser.element('#BillingNewAddress_ZipPostalCode').send_keys(zipcode)

    @allure.step('Fill in phone number: {phone_number}')
    def _fill_in_phone_number(self, phone_number):
        browser.element('#BillingNewAddress_PhoneNumber').send_keys(phone_number)

    @allure.step('Click on billing address Continue button')
    def _click_on_billing_address_continue_button(self):
        browser.element(
            '#billing-buttons-container .new-address-next-step-button'
        ).click()

    @allure.step('Click on shipping address Continue button')
    def _click_on_shipping_address_continue_button(self):
        browser.element(
            '#shipping-buttons-container .new-address-next-step-button'
        ).click()

    @allure.step('Click on shipping method Continue button')
    def _click_on_shipping_method_continue_button(self):
        browser.element('.shipping-method-next-step-button').click()

    @allure.step('Click on payment method Continue button')
    def _click_on_payment_method_continue_button(self):
        browser.element('.payment-method-next-step-button').click()

    @allure.step('Click on payment info Continue button')
    def _click_on_payment_info_continue_button(self):
        browser.element('.payment-info-next-step-button').click()

    @allure.step('Click on Confirm button')
    def _click_on_confirm_button(self):
        browser.element('.confirm-order-next-step-button').click()

    @allure.step('Go through checkout process without billing address previously saved')
    def go_through_checkout_process_without_billing_address(self, user):
        self._select_country(user.country)
        self._fill_in_city(user.city)
        self._fill_in_address1(user.address1)
        self._fill_in_zipcode(user.zipcode)
        self._fill_in_phone_number(user.phone_number)
        self._click_on_billing_address_continue_button()
        self._click_on_shipping_address_continue_button()
        self._click_on_shipping_method_continue_button()
        self._click_on_payment_method_continue_button()
        self._click_on_payment_info_continue_button()
        self._click_on_confirm_button()

    @allure.step('Go through checkout process with billing address already saved')
    def go_through_checkout_process_with_billing_address_already_saved(self):
        self._click_on_billing_address_continue_button()
        self._click_on_shipping_address_continue_button()
        self._click_on_shipping_method_continue_button()
        self._click_on_payment_method_continue_button()
        self._click_on_payment_info_continue_button()
        self._click_on_confirm_button()
