import time
import URLs
from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPage
import allure

class TestOrder:
    @allure.title('Проверка флоу создания заказа сценарий 1')
    @allure.description('На главной странице принимаем cookie, нажимаем кнопку "Заказать" вверху экрана, заполняем поля и проверяем, что заказ оформляется')
    def test_make_order_with_up_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_order_up_button()
        order_page.data_input_for_whom_test1()
        order_page.data_input_about_rent_test1()

        assert order_page.approval_message

    @allure.title('Проверка флоу создания заказа сценарий 2')
    @allure.description('На главной странице принимаем cookie, нажимаем кнопку "Заказать" внизу экрана, заполняем поля и проверяем, что заказ оформляется')
    def test_make_order_with_down_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_order_down_button()
        order_page.data_input_for_whom_test2()
        order_page.data_input_about_rent_test2()

    @allure.title('Проверка перехода по лого самоката')
    @allure.description('На главной странице нажимаем кнопку "Заказать", нажимаем на лого самокат и проверяем, что произошел переход на Главную страницу')
    def test_logo_samokat(self,driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_order_up_button()
        order_page.scooter_logo_click()

        assert main_page.get_current_url()==URLs.URL_BASE_SLASH

    @allure.title('Проверка перехода по лого яндекс')
    @allure.description('На главной странице нажимаем кнопку "Заказать", нажимаем на лого яндекс и проверяем, что произошел переход на новую вкладку Дзен')
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_order_up_button()
        order_page.yandex_logo_click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)
        assert driver.current_url == URLs.DZEN_URL



