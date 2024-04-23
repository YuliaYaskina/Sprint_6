from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class MainPage (BasePage):

    order_up_button = [By.CLASS_NAME, 'Button_Button__ra12g']
    order_down_button = [By.XPATH, ".//div[@class = 'Home_FinishButton__1_cWm']"]
    cookies_accept_button = [By.XPATH, ".//button[text()='да все привыкли']"]
    questions_area = [By.XPATH, ".//div[@class ='Home_SubHeader__zwi_E']"]
    question = [By.ID, "accordion__panel-0"]

    @allure.step('Нажимаем кнопку "Заказать вверху страницы')
    def click_order_up_button(self):
        self.driver.find_element(*self.order_up_button).click()

    @allure.step('Нажимаем кнопку "Заказать внизу страницы')
    def click_order_down_button(self):
        self.driver.find_element(*self.order_down_button).click()

    @allure.step('Соглашаемся с использованием cookie')
    def accept_cookies(self):
        self.driver.find_element(*self.cookies_accept_button).click()

    @allure.step('Пролистываем до нужного элемента на странице')
    def scroll(self):
        element = self.driver.find_element(*self.questions_area)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажимаем на вопрос')
    def click_question(self, i):
        question = (By.ID, f"accordion__heading-{i}")
        answer = (By.ID, f"accordion__panel-{i}")
        self.driver.find_element(*question).click()
        return self.driver.find_element(*answer).text






