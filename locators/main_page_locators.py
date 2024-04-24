from selenium.webdriver.common.by import By


class MainPageLocators:
    question_locator = [By.ID, 'accordion__heading-{}']
    answer_locator = [By.ID, 'accordion__panel-{}']
    ORDER_UP_BUTTON_LOCATOR = [By.CLASS_NAME, 'Button_Button__ra12g']
    order_down_button_locator = [By.XPATH, ".//div[@class = 'Home_FinishButton__1_cWm']"]
    cookies_accept_button_locator = [By.XPATH, ".//button[text()='да все привыкли']"]
    questions_area_locator = [By.XPATH, ".//div[@class ='Home_SubHeader__zwi_E']"]

