import pytest

from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.maximize_window()

    yield driver

    driver.close()





