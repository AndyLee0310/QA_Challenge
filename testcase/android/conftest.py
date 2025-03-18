import logging
import time
import pytest
from appium import webdriver

driver = None

@pytest.fixture()
def open_app(android_setting):
    global driver
    driver = webdriver.Remote('http://localhost:4723', options=android_setting)
    logging.info('driver start')
    return driver

@pytest.fixture()
def close_app():
    yield driver
    time.sleep(2)
    driver.quit()
    logging.info('driver quit')
