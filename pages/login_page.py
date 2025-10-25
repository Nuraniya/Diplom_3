import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Выполнить вход")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()