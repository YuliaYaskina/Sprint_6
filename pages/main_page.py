
from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators as Locators, MainPageLocators


class MainPage (BasePage):

    @allure.step('Получаем текст ответа на вопрос')
    def get_answer_text(self, locator_q, locator_a, num):
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)

        self.find_element_with_wait(locator_q_formatted).click()
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Получаем вопос по локатору')
    def get_question(self):
        qst = MainPageLocators.question_locator
        return qst

    @allure.step('Получаем ответ по локатору')
    def get_answer(self):
        answ = MainPageLocators.answer_locator
        return answ

    @allure.step('Нажимаем кнопку "Заказать вверху страницы')
    def click_order_up_button(self):
        self.find_element_with_wait(Locators.order_up_button_locator).click()

    @allure.step('Нажимаем кнопку "Заказать внизу страницы')
    def click_order_down_button(self):
        self.find_element_with_wait(Locators.order_down_button_locator).click()

    @allure.step('Соглашаемся с использованием cookie')
    def accept_cookies(self):
        self.find_element_with_wait(Locators.cookies_accept_button_locator).click()









