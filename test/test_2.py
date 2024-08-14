import pytest
from selenium import webdriver
from pages.shop_luma import ShopLuma


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_filter(driver):
    filter_item = ShopLuma(driver)
    filter_item.open_page()
    filter_item.filter()

def test_compare(driver):
    compare = ShopLuma(driver)
    compare.open_page()
    compare.compare_luma()

def test_wishlist(driver):
    compare = ShopLuma(driver)
    compare.open_page()
    compare.wishlist_luma('You must login or register to add items to your wishlist.')
