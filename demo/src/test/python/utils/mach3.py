import logging
import os
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver

class Mach3Page:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.gillette.co.in")

    def hover_products(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            ele1_xpath = "//span[contains(text(),'Products')]"
            ele2_xpath = "/html[1]/body[1]/div[1]/header[1]/div[1]/nav[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[3]"
            ele1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, ele1_xpath)))
            actions = ActionChains()
            actions.move_to_element(ele1).perform()
            ele2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, ele2_xpath)))
            ele2.click()
            logging.info("Hovered successfully.")

        except Exception as e:
            self.driver.save_screenshot("screenshot.png")
            
            
    
    def click_product(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='__next']/main[@id='main-content']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/span[1]")))
            search_box.click()
            logging.info("Clicked product successfully.")

        except Exception as e:
            self.driver.save_screenshot("screenshot.png")

if __name__ == "__main__":
    unittest.main()
