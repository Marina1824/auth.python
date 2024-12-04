import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.shop_luma import ShopLuma
from pages.sales import Sales
from pages.customer_login import Customerlogin
from time import sleep


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    sleep(3)
    chrome_driver.implicitly_wait(5)
    return chrome_driver


@pytest.fixture()
def shop_luma(driver):
    return ShopLuma(driver)


@pytest.fixture()
def sales(driver):
    return Sales(driver)


@pytest.fixture()
def login_page(driver):
    return Customerlogin(driver)
