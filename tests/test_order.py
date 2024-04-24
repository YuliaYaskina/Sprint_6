
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
        assert order_page.get_check_status_message() == 'Посмотреть статус'

    @allure.title('Проверка флоу создания заказа сценарий 2')
    @allure.description('На главной странице принимаем cookie, нажимаем кнопку "Заказать" внизу экрана, заполняем поля и проверяем, что заказ оформляется')
    def test_make_order_with_down_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_order_down_button()
        order_page.data_input_for_whom_test2()
        order_page.data_input_about_rent_test2()

        assert order_page.get_check_status_message() == 'Посмотреть статус'




