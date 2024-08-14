import pytest
from selenium import webdriver
from pages.sales import Sales


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_url(driver):
    login_page = Sales(driver)
    login_page.open_page()
    login_page.items('https://magento.softwaretestingboard.com/promotions/women-sale.html')


def test_title(driver):
    login_page = Sales(driver)
    login_page.open_page()
    login_page.jackets()


def test_compare_delete(driver):
    login_page = Sales(driver)
    login_page.open_page()
    login_page.compare_delete()
