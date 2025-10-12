from selenium.webdriver.common.by import By


class MainPageLocators:
    # Основные кнопки навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")

    # Ингредиенты
    INGREDIENT = (By.XPATH, "//p[contains(@class, 'BurgerIngredient_ingredient__text')]")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient__')]")
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter_counter__num__3nue1")

    # Конструктор
    CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    # Модальные окна
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    ORDER_SUCCESS_MODAL = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_')]")

    # Разделы
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")