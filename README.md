## Дипломный проект. Задание 3: UI-тесты

## Студент: Нурания Сулейманова

## Когорта: №29

## # Stellar Burgers UI Tests

## Инструкция по запуску:

### Установите зависимости:

> pip install -r requirements.txt

### Запустить все тесты:

> pytest -v

### Посмотреть отчет по прогону html

> allure serve allure_results

Project files and description:

| Название файла          | Содержание файла               |
|-------------------------|--------------------------------|
| Tests                   | Директория с тестами           |
| test_create_bookings.py | Тесты на создание бронирования |
| test_delete_booking.py  | Тесты на удаление бронирования |
| conftest.py             | Фикстуры                       |
| helpers.py              | Хэлпер для тела запросов       |
| data.py                 | Файл с URL и body запросов     |
| auth_methods.py         | http клиент к auth методам     |
| booking_methods.py      | http клиент к booking методам  |
| generators.py           | Генератор данных               |
| requirements.txt        | Файл с зависимостями           |
| allure_results.dir      | Папка с отчетами Allure        |

# Stellar Burgers UI Tests

Автотесты для веб-приложения Stellar Burgers.

## Структура проекта
- `pages/` - Page Object классы
- `tests/` - тестовые модули и конфигурация pytest
- `data.py` - тестовые данные

## Запуск тестов
```bash
# Установка зависимостей
pip install -r requirements.txt

# Все тесты
pytest

# С генерацией Allure отчета
pytest --alluredir=allure-results
allure serve allure-results

# Тесты для конкретного браузера
pytest --browser=chrome
pytest --browser=firefox