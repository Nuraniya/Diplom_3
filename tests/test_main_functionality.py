import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


@allure.suite("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_constructor_navigation(self, main_page, order_feed_page):
        main_page.click_order_feed_button()
        main_page.wait.until(EC.url_contains("/feed"))
        main_page.click_constructor_button()

        assert main_page.is_buns_section_displayed()

    @allure.title("Переход по клику на раздел 'Лента заказов'")
    def test_order_feed_navigation(self, main_page, order_feed_page):
        main_page.click_order_feed_button()
        main_page.wait.until(EC.url_contains("/feed"))

        assert order_feed_page.is_order_feed_displayed()

    @allure.title("Открытие всплывающего окна с деталями ингредиента")
    def test_ingredient_modal_opening(self, main_page):
        main_page.click_ingredient()

        assert main_page.is_modal_visible()

    @allure.title("Закрытие всплывающего окна по клику на крестик")
    def test_ingredient_modal_closing(self, main_page):
        main_page.click_ingredient()
        main_page.close_ingredient_modal()

        assert main_page.wait_for_element_invisible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.title("Увеличение счетчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increase(self, main_page, login):
        initial_counter = main_page.get_ingredient_counter()
        main_page.drag_ingredient_to_constructor()
        updated_counter = main_page.get_ingredient_counter()

        assert updated_counter > initial_counter