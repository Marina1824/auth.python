import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_auth(driver):
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
    first = "Test"
    last = "Testov"
    email = 'test543@yandex.ru'
    password = 'privet!!@2222'
    confirm_pas = 'privet!!@2222'

    first_name = driver.find_element(By.ID, 'firstname')
    first_name.send_keys(first)
    last_name = driver.find_element(By.ID, 'lastname')
    last_name.send_keys(last)
    email_field = driver.find_element(By.ID, 'email_address')
    email_field.send_keys(email)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)
    confirm_field = driver.find_element(By.ID, 'password-confirmation')
    confirm_field.send_keys(confirm_pas)
    submit = driver.find_element(By.CLASS_NAME, 'submit')
    submit.click()
    registering = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div'))
    )
    assert registering.text == "Thank you for registering with Main Website Store."
    sleep(3)
