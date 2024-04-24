from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class OrderPage (BasePage):
    name_field = [By.XPATH, ".//input[@placeholder='* Имя']"]
    surname_field = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    address_field = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_field = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    metro_cherkizovskaya = [By.XPATH,".//div[text()='Черкизовская']"]
    metro_sokolniki = [By.XPATH,".//div[text()='Сокольники']"]
    phone_field = [By.XPATH,"//input[@placeholder='* Телефон: на него позвонит курьер']"]
    go_on_button = [By.XPATH,".//button[text()='Далее']"]
    when_field = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    data_picker_day01 = [By.XPATH, ".//div[@class = 'react-datepicker__day react-datepicker__day--001']"]
    data_picker_day30 = [By.XPATH,".//div[@class = 'react-datepicker__day react-datepicker__day--030']"]
    period_field = [By.XPATH, ".//div[text()='* Срок аренды']"]
    period_sutki_field = [By.XPATH, ".//div[text()='сутки']"]
    period_7sutok_field = [By.XPATH, ".//div[text()='семеро суток']"]
    colour_field_black = [By.XPATH, ".//label[@for='black']"]
    colour_field_grey = [By.XPATH, ".//label[@for='grey']"]
    comment_field = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    make_order_button = [By.XPATH, ".//button[2][text()='Заказать']"]
    approval_button = [By.XPATH,".//button[text()='Да']"]
    check_status_button = [By.XPATH,".//button[text()='Посмотреть статус']"]
    scooter = [By.XPATH,".//img[@alt='Scooter']"]
    yandex = [By.XPATH,".//img[@alt='Yandex']"]

    @allure.step('Получить текст сообщения об оформлении заказа')
    def get_check_status_message(self):
        button_text = self.driver.find_element(*self.check_status_button)
        return button_text.text
    @allure.step('Нажимаем на лого самоката')
    def scooter_logo_click(self):
        self.driver.find_element(*self.scooter).click()

    @allure.step('Нажимаем на лого яндекса')
    def yandex_logo_click(self):
        self.driver.find_element(*self.yandex).click()

    @allure.step('Заполняем страницу Для кого самокат')
    def data_input_for_whom_test1(self):
        self.driver.find_element(*self.name_field).send_keys("Имя")
        self.driver.find_element(*self.surname_field).send_keys("Фамилия")
        self.driver.find_element(*self.address_field).send_keys("Москва, ул.Крылатская, д.1, кв.1")
        self.driver.find_element(*self.metro_field).click()
        self.driver.find_element(*self.metro_cherkizovskaya).click()
        self.driver.find_element(*self.phone_field).send_keys("89002223333")
        self.driver.find_element(*self.go_on_button).click()

    @allure.step('Заполняем страницу Про аренду')
    def data_input_about_rent_test1(self):
        self.driver.find_element(*self.when_field).click()
        self.driver.find_element(*self.data_picker_day01).click()
        self.driver.find_element(*self.period_field).click()
        self.driver.find_element(*self.period_sutki_field).click()
        self.driver.find_element(*self.colour_field_black).click()
        self.driver.find_element(*self.comment_field).send_keys("комментарий")
        self.driver.find_element(*self.make_order_button).click()
        self.driver.find_element(*self.approval_button).click()

    @allure.step('Заполняем страницу Для кого самокат')
    def data_input_for_whom_test2(self):
        self.driver.find_element(*self.name_field).send_keys("Двойное Имя")
        self.driver.find_element(*self.surname_field).send_keys("фамилия")
        self.driver.find_element(*self.address_field).send_keys("Крылатская, 1")
        self.driver.find_element(*self.metro_field).click()
        self.driver.find_element(*self.metro_sokolniki).click()
        self.driver.find_element(*self.phone_field).send_keys("+79874561212")
        self.driver.find_element(*self.go_on_button).click()

    @allure.step('Заполняем страницу Про аренду')
    def data_input_about_rent_test2(self):
        self.driver.find_element(*self.when_field).click()
        self.driver.find_element(*self.data_picker_day30).click()
        self.driver.find_element(*self.period_field).click()
        self.driver.find_element(*self.period_7sutok_field).click()
        self.driver.find_element(*self.colour_field_grey).click()
        self.driver.find_element(*self.comment_field).send_keys("-")
        self.driver.find_element(*self.make_order_button).click()
        self.driver.find_element(*self.approval_button).click()



