import allure
from selene import browser, have, be


class RegistrationPage:
    @allure.step('Open Registration page')
    def open(self):
        browser.element('.ico-register').click()

    @allure.step('Fill in first name: {first_name}')
    def _fill_in_first_name(self, first_name):
        browser.element('#FirstName').send_keys(first_name)

    @allure.step('Fill in last name: {last_name}')
    def _fill_in_last_name(self, last_name):
        browser.element('#LastName').send_keys(last_name)

    @allure.step('Fill in email: {email}')
    def _fill_in_email(self, email):
        browser.element('#Email').send_keys(email)

    @allure.step('Fill in password: {password}')
    def _fill_in_password(self, password):
        browser.element('#Password').send_keys(password).press_tab()

    @allure.step('Fill in confirm password: {password}')
    def _fill_in_confirm_password(self, password):
        browser.element('#ConfirmPassword').send_keys(password).press_tab()

    @allure.step('Choose gender: {gender}')
    def _choose_gender(self, gender):
        browser.element(f'#gender-{gender}+label').click()

    @allure.step('Click on Register button')
    def _click_on_register_button(self):
        browser.element('#register-button').click()

    @allure.step('User validation error should render')
    def user_validation_error_should_render(self):
        browser.element('.message-error li').should(
            have.exact_text('The specified email already exists')
        )

    @allure.step('User has successfully registered')
    def user_has_successfully_registered(self):
        browser.element('.page-title h1').should(have.exact_text('Register'))
        browser.element('div .result').should(
            have.exact_text('Your registration completed')
        )
        browser.element('.register-continue-button').should(be.clickable)

    @allure.step('Register user')
    def register_user(self, user):
        self.open()
        self._choose_gender(user.gender)
        self._fill_in_first_name(user.first_name)
        self._fill_in_last_name(user.last_name)
        self._fill_in_email(user.email)
        self._fill_in_password(user.password)
        self._fill_in_confirm_password(user.password)
        self._click_on_register_button()
