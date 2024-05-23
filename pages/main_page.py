
from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators as Locators


class MainPage (BasePage):

    @allure.step('Получаем текст ответа на вопрос')
    def get_answer_text(self,num):
        locator_q_formatted = self.format_locators(Locators.question_locator, num)
        locator_a_formatted = self.format_locators(Locators.answer_locator, num)

        self.find_element_with_wait(locator_q_formatted).click()
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Нажимаем кнопку "Заказать вверху страницы')
    def click_order_up_button(self):
        self.find_element_with_wait(Locators.order_up_button_locator).click()

    @allure.step('Нажимаем кнопку "Заказать внизу страницы')
    def click_order_down_button(self):
        self.find_element_with_wait(Locators.order_down_button_locator).click()

    @allure.step('Соглашаемся с использованием cookie')
    def accept_cookies(self):
        self.find_element_with_wait(Locators.cookies_accept_button_locator).click()









