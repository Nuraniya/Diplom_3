from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_SECTION = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[1]")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[1]")
    ORDERS_IN_PROGRESS = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__')]")