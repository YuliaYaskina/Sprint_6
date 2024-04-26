import urls
from conftest import driver
from pages.main_page import MainPage
import allure
from pages.base_page import BasePage
from pages.order_page import OrderPage

class TestRedirect:
    @allure.title('Проверка перехода по лого самоката')
    @allure.description('На главной странице нажимаем кнопку "Заказать", нажимаем на лого самокат и проверяем, что произошел переход на Главную страницу')
    def test_logo_samokat(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_order_up_button()
        order_page.scooter_logo_click()

        assert main_page.get_current_url() == urls.URL_BASE

    @allure.title('Проверка перехода по лого яндекс')
    @allure.description('На главной странице нажимаем кнопку "Заказать", нажимаем на лого яндекс и проверяем, что произошел переход на новую вкладку Дзен')
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_order_up_button()
        order_page.yandex_logo_click()
        order_page.switch_page()

        assert main_page.get_current_url() == urls.DZEN_URL