from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ShopLuma:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')

    def filter(self):
        new = self.driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[9]')
        new.click()
        yes = self.driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[9]/div[2]/ol/li[1]/a')
        yes.click()
        sleep(5)

    def check_success_text(self, expected_text):
        registering = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div'))

        )
        assert registering.text == expected_text

    def check_text(self, expected_text):
        registering = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[2]'))

        )
        assert registering.text == expected_text

    def check_email(self, expected_text):
        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="email_address-error"]'))
        )
        assert email.text == expected_text
