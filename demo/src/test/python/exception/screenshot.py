from selenium import webdriver
import datetime
import os
import sys

class Screenshot:
    @staticmethod
    def capture_screenshot(driver):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Define the screenshot directory path
        screenshot_dir = "/home/coder/project/workspace/demo/main/Reports"

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        screenshot_filename = f"screenshot_{timestamp}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
        print(f"Screenshot saved to: {screenshot_path}")

        driver.save_screenshot(screenshot_path)
        return screenshot_path

if __name__ == "__main__":
    # Initialize WebDriver and open a webpage
    # driver = webdriver.Chrome()
    # driver.get("https://www.example.com")

    # # Capture a screenshot and save it in the specified directory
    # Screenshot.capture_screenshot(driver)

    # # Close the WebDriver
    driver.quit()
