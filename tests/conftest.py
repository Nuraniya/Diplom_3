import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser type: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = None

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_options)


    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")

        firefox_options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

        driver = webdriver.Firefox(options=firefox_options)

    driver.implicitly_wait(10)
    driver.get("https://stellarburgers.education-services.ru")

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="function")
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture(scope="function")
def login(main_page, login_page):
    main_page.click_login_button()
    login_page.login("test_user_12345@example.com", "password123")
    main_page.wait.until(EC.url_contains("/"))