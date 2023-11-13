import allure
from selene import browser, have


class LoginPage:
    @allure.step('Open Login page')
    def open(self):
        browser.element('.ico-login').click()

    @allure.step('Fill in email: {email}')
    def _fill_in_email(self, email):
        browser.element('#Email').send_keys(email)

    @allure.step('Fill in password: {password}')
    def _fill_in_password(self, password):
        browser.element('#Password').send_keys(password)

    @allure.step('Click on Login button')
    def _click_on_login_button(self):
        browser.element('.login-button').click()

    @allure.step('Invalid credentials error should render')
    def invalid_credentials_error_renders(self):
        browser.element('.validation-summary-errors').should(
            have.exact_text(
                'Login was unsuccessful. Please correct the errors and try again.\nThe credentials provided are incorrect',
            )
        )

    @allure.step('No account error should render')
    def no_account_error_renders(self):
        browser.element('.validation-summary-errors').should(
            have.exact_text(
                'Login was unsuccessful. Please correct the errors and try again.\nNo customer account found',
            )
        )

    @allure.step('Log in as user')
    def log_in(self, user):
        self.open()
        self._fill_in_email(user.email)
        self._fill_in_password(user.password)
        self._click_on_login_button()

    @allure.step('User has successfully logged in')
    def user_has_successfully_logged_in(self, user):
        browser.element('.header .account').should(have.exact_text(user.email))
