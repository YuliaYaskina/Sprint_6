import pytest
from selenium import webdriver
import urls

@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.fullscreen_window()
    firefox_driver.get(urls.URL_BASE)


    yield firefox_driver

    firefox_driver.quit()