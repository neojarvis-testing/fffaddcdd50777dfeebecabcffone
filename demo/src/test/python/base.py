import os
import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from exception.logger import configure_logger
from utils.gillete_page import GillettePage
from utils.mach3 import Mach3Page
from exception.eventhandler import EventHandler
from utils.hairstyle import HairStylePage
from webdriver_manager.chrome import ChromeDriverManager

class TestGilletteSearch(unittest.TestCase):
      
    def setUp(self):
        event_handler = EventHandler()
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        capabilities = {
            "browserName": "chrome",
            "platform": "ANY",
            "version": "",
        }      
      
        remote_url = "http://34.85.201.58:4499"
        
        self.driver = webdriver.Remote(
            command_executor=remote_url,
            options=options
        )
       
        self.driver = EventFiringWebDriver(self.driver, event_handler)       

        self.gillette_page = GillettePage(self.driver)
        self.mach3 = Mach3Page(self.driver)
        self.hairstyle = HairStylePage(self.driver)

    def test_gillette_search(self):
        self.gillette_page.open()
        self.gillette_page.click_search_box()
        self.gillette_page.enter_search_query('razor')
        self.gillette_page.submit_search()
        time.sleep(5)

    def test_mach3_search(self):  
        self.mach3.open()
        self.mach3.hover_products()
        self.mach3.click_product()
        time.sleep(5)

    def test_hairstyle_search(self):
        self.hairstyle.open()
        self.hairstyle.click_Styles() 
        self.hairstyle.click_facial()
        time.sleep(5)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    log_dir = "/home/coder/project/workspace/demo/main/logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    configure_logger(log_dir)

    # Test reports start
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGilletteSearch)
    report_dir = "/home/coder/project/workspace/demo/main/screenshot"
    test_runner = HtmlTestRunner.HTMLTestRunner(
        output=report_dir, 
        report_title="Test Report",
        descriptions="Test execution report"
    )
    test_result = test_runner.run(suite)


