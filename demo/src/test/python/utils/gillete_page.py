import logging
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GillettePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.gillette.co.in")

    def click_search_box(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            search_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Search here']")))
            search_icon.click()
            logging.info("clicked on Search icon successfully.")
        except Exception as e:
            self.driver.save_screenshot("screenshot.png")

    def enter_search_query(self, query):
        try:
            wait = WebDriverWait(self.driver, 30)
            search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='search-box-input']")))
            search_box.send_keys(query)
            logging.info("keys sent to the Search box successfully")
        except Exception as e:
            self.driver.save_screenshot("screenshot.png")

    def submit_search(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='Razor']")))
            search_box.click()
            logging.info("Search for Razor successfully")
        except Exception as e:
            self.driver.save_screenshot("screenshot.png")

# class TestGillettePage(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()  # Change this based on your preferred browser driver
#         self.gillette_page = GillettePage(self.driver)

#     def tearDown(self):
#         self.driver.quit()

   

if __name__ == "__main__":
    unittest.main()
