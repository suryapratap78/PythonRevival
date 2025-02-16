import pytest
import home_page
def test_homepage_tile(driver):
    driver.get('https://www.amazon.in/')
    homepage_title = home_page.validate_homepage_title(driver)
    assert homepage_title.__contains__('Online Shopping site')


def test_cart_default_count(driver):
    driver.get('https://www.amazon.in/')
    cart_item_count = home_page.get_cart_item_count(driver)
    assert cart_item_count == 0




