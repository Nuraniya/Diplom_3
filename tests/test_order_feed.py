import allure
from selenium.webdriver.support import expected_conditions as EC


class TestOrderFeed:

    @allure.title("Проверка отображения счетчиков заказов")
    def test_total_orders_counter_increase(self, main_page, order_feed_page):
        main_page.click_order_feed_button()
        main_page.wait.until(EC.url_contains("/feed"))

        total_orders = order_feed_page.get_total_orders_count()
        today_orders = order_feed_page.get_today_orders_count()

        assert total_orders >= 0
        assert today_orders >= 0

    @allure.title("Проверка раздела 'В работе'")
    def test_today_orders_counter_increase(self, main_page, order_feed_page):
        main_page.click_order_feed_button()
        main_page.wait.until(EC.url_contains("/feed"))

        orders_in_progress = order_feed_page.get_orders_in_progress()
        assert orders_in_progress is not None

    @allure.title("Проверка навигации по ленте заказов")
    def test_order_appears_in_progress(self, main_page, order_feed_page):
        main_page.click_order_feed_button()
        main_page.wait.until(EC.url_contains("/feed"))

        assert order_feed_page.is_order_feed_displayed()