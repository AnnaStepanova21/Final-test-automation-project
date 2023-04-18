import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def start_page():
    driver = webdriver.Chrome('C:\\Users\\celev\\PycharmProjects\\chromedriver.exe')
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    yield driver
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    driver.quit()
