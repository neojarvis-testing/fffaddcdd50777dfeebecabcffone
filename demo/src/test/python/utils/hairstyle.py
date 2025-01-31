import os
import logging
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from exception.eventhandler import EventHandler
from exception.screenshot import Screenshot


class HairStylePage:
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get("https://www.gillette.co.in")

    def click_Styles(self):
        try:
            # wait = WebDriverWait(self.driver, 10)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait = WebDriverWait(self.driver, 10)
            click_style = wait.until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='__next']/footer[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")))
            click_style.click()
            logging.info("scrolled down successfully.")

        
        except Exception as e:
            self.save_screenshot("screenshot.png")

    def click_facial(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            click_facial = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='tabItem_1']")))
            click_facial.click()
            logging.info("clicked facial successfully.")

        except Exception as e:
            self.save_screenshot("screenshot.png")

  
if __name__ == "__main__":
    unittest.main()
