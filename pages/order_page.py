
from locators.order_page_locators import OrderPageLocators
from locators.dzen_locators import DzenLocators
from pages.base_page import BasePage
import allure


class OrderPage (BasePage):
    @allure.step('Переключаемся на вкладку Дзен')
    def switch_page(self):
        self.switch_to_window(DzenLocators.NEWS)
    @allure.step('Получить текст сообщения об оформлении заказа')
    def get_check_status_message(self):
        button_text = self.find_element_with_wait(OrderPageLocators.check_status_button)
        return button_text.text
    @allure.step('Нажимаем на лого самоката')
    def scooter_logo_click(self):
        self.find_element_with_wait(OrderPageLocators.scooter).click()

    @allure.step('Нажимаем на лого яндекса')
    def yandex_logo_click(self):
        self.find_element_with_wait(OrderPageLocators.yandex).click()

    @allure.step('Заполняем страницу Для кого самокат')
    def data_input_for_whom_test1(self):
        self.find_element_with_wait(OrderPageLocators.name_field).send_keys("Имя")
        self.find_element_with_wait(OrderPageLocators.surname_field).send_keys("Фамилия")
        self.find_element_with_wait(OrderPageLocators.address_field).send_keys("Москва, ул.Крылатская, д.1, кв.1")
        self.find_element_with_wait(OrderPageLocators.metro_field).click()
        self.find_element_with_wait(OrderPageLocators.metro_cherkizovskaya).click()
        self.find_element_with_wait(OrderPageLocators.phone_field).send_keys("89002223333")
        self.find_element_with_wait(OrderPageLocators.go_on_button).click()

    @allure.step('Заполняем страницу Про аренду')
    def data_input_about_rent_test1(self):
        self.find_element_with_wait(OrderPageLocators.when_field).click()
        self.find_element_with_wait(OrderPageLocators.data_picker_day01).click()
        self.find_element_with_wait(OrderPageLocators.period_field).click()
        self.find_element_with_wait(OrderPageLocators.period_sutki_field).click()
        self.find_element_with_wait(OrderPageLocators.colour_field_black).click()
        self.find_element_with_wait(OrderPageLocators.comment_field).send_keys("комментарий")
        self.find_element_with_wait(OrderPageLocators.make_order_button).click()
        self.find_element_with_wait(OrderPageLocators.approval_button).click()

    @allure.step('Заполняем страницу Для кого самокат')
    def data_input_for_whom_test2(self):
        self.find_element_with_wait(OrderPageLocators.name_field).send_keys("Двойное Имя")
        self.find_element_with_wait(OrderPageLocators.surname_field).send_keys("фамилия")
        self.find_element_with_wait(OrderPageLocators.address_field).send_keys("Крылатская, 1")
        self.find_element_with_wait(OrderPageLocators.metro_field).click()
        self.find_element_with_wait(OrderPageLocators.metro_sokolniki).click()
        self.find_element_with_wait(OrderPageLocators.phone_field).send_keys("+79874561212")
        self.find_element_with_wait(OrderPageLocators.go_on_button).click()

    @allure.step('Заполняем страницу Про аренду')
    def data_input_about_rent_test2(self):
        self.find_element_with_wait(OrderPageLocators.when_field).click()
        self.find_element_with_wait(OrderPageLocators.data_picker_day30).click()
        self.find_element_with_wait(OrderPageLocators.period_field).click()
        self.find_element_with_wait(OrderPageLocators.period_7sutok_field).click()
        self.find_element_with_wait(OrderPageLocators.colour_field_grey).click()
        self.find_element_with_wait(OrderPageLocators.comment_field).send_keys("-")
        self.find_element_with_wait(OrderPageLocators.make_order_button).click()
        self.find_element_with_wait(OrderPageLocators.approval_button).click()



