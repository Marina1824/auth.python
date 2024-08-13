import pytest
from selenium import webdriver
from pages.shop_luma import ShopLuma


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_auth(driver):
    filter_item = ShopLuma(driver)
    filter_item.open_page()
    filter_item.filter()
