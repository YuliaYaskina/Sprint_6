import urls
from conftest import driver
from pages.main_page import MainPage
import allure


class TestMain:
    @allure.title('Проверка перехода по кнопке Заказать вверху экрана')
    @allure.description('На главной странице нажимаем кнопку "Заказать" и проверяем, что сработал переход на форму оформления заказа')
    def test_click_order_up_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_up_button()
        assert main_page.get_current_url() == urls.URL_ORDER

    @allure.title('Проверка перехода по кнопке Заказать внизу экрана')
    @allure.description('На главной странице нажимаем кнопку "Заказать" и проверяем, что сработал переход на форму оформления заказа')
    def test_click_order_down_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_down_button()
        assert main_page.get_current_url() == urls.URL_ORDER










