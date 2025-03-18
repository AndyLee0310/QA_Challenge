import os
import allure
import logging
from time import sleep
from module import path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Common:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, element, timeout=30):
        """
        Wait for an element to be displayed

        If element is a WebElement, check its visibility; 
        if it is a locator, first find the element and then check its visibility
        """
        try:
            if isinstance(element, tuple):  # If the input is a locator condition (By, 'value')
                WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(element)
                )
            else:  # If the input is a WebElement, directly check its visibility
                WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of(element)
                )
        except TimeoutException:
            logging.error(TimeoutException(f"Element {element} did not appear within {timeout} seconds"))
            return False

    def take_screenshot(self, screenshot_name, sleep_time=3):
        """
        Take a screenshot and save it
        - screenshot_name: screenshot name
        """
        screenshot_dir = os.path.join(path.SCREENSHOT)
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        screenshot_path = os.path.join(screenshot_dir, f'{screenshot_name}.png')
        sleep(sleep_time)
        self.driver.get_screenshot_as_file(screenshot_path)  # Save it as an image
        logging.info(f"Screenshot has been saved to: {screenshot_path}")

        # Attach the screenshot to the allure report
        with open(screenshot_path, "rb") as screenshot_file:
            allure.attach(screenshot_file.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
