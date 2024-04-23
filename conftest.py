import pytest
from selenium import webdriver
import URLs

@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.fullscreen_window()
    firefox_driver.get(URLs.URL_BASE)


    yield firefox_driver

    firefox_driver.quit()