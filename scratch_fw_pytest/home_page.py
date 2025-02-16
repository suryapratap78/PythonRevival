from selenium import webdriver
from selenium.webdriver.common.by import By

#homepage locators

cart_item_count_id = 'nav-cart-count'


def validate_homepage_title(driver :webdriver):
    return driver.title

def get_cart_item_count(driver):
    if driver.find_element(By.ID('nav-cart')).is_displayed():
        return driver.find_element(By.ID(cart_item_count_id)).text




