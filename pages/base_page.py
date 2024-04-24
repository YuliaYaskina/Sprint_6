from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from locators.main_page_locators import MainPageLocators


class BasePage:
    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем элемент после ожидания')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator) #2.Когда ставить *?

    @allure.step('Кликаем на элемент')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until((expected_conditions.element_to_be_clickable(locator)))
        self.driver.find_element(locator).click()

    @allure.step('Заполняем поле')
    def add_text_to_element(self, locator):
        self.find_element_with_wait(locator).send_keys(text) #1.Почему без driver?

    @allure.step('Получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключаемся на последнюю вкладку браузера')
    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Пролистываем до нужного элемента на странице')
    def scroll(self):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)

        return (method, locator)


