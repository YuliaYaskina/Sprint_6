from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators as Locators

class MainPage (BasePage):

    @allure.step('Получаем текст ответа на вопрос')
    def get_answer_text(self, locator_q, locator_a, num):
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)

        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Нажимаем кнопку "Заказать вверху страницы')
    def click_order_up_button(self):
        self.find_element_with_wait(Locators.ORDER_UP_BUTTON_LOCATOR)
        self.click_to_element(Locators.ORDER_UP_BUTTON_LOCATOR)

    @allure.step('Нажимаем кнопку "Заказать внизу страницы')
    def click_order_down_button(self, order_down_button_locator):
        self.click_to_element(order_down_button_locator)

    @allure.step('Соглашаемся с использованием cookie')
    def accept_cookies(self, cookies_accept_button_locator):
        self.click_to_element(cookies_accept_button_locator)

    @allure.step('Пролистываем до нужного элемента на странице')
    def scroll_to_questions(self, questions_area_locator):
        self.scroll(questions_area_locator)








