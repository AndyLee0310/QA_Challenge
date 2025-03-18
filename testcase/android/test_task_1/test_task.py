import allure
import pytest
from time import sleep
from datetime import datetime, timedelta
from module.common import Common
from page.declaration_page import DeclarationPage
from page.alert_page import AlertPage
from page.home_page import HomePage
from page.forecast_page import ForecastPage

@allure.feature("QA Challenge")
class TestTask1():

    @allure.story("task_1")
    @allure.title("[task 1]Check the 9th day's weather forecast from 9-day forecast screen")
    @pytest.mark.task1
    def test_check_weather_for_day_nine(self, open_app, close_app):
        driver = open_app
        common = Common(driver)
        disclaimer_page = DeclarationPage(driver)
        alert_page = AlertPage(driver)
        home_page = HomePage(driver)
        forecast_page = ForecastPage(driver)

        with allure.step('Agree to the disclaimer'):
            if disclaimer_page.page_title.is_displayed():
                disclaimer_page.wait_for_page_to_load()
                common.take_screenshot(f'Disclaimer')
                disclaimer_page.agree_button.click()
        
        with allure.step('Agree to the privacy policy statement'):
            if disclaimer_page.page_title.is_displayed():
                disclaimer_page.wait_for_page_to_load()
                common.take_screenshot(f'Privacy policy statement')
                disclaimer_page.agree_button.click()

        with allure.step('Agree to background location access'):
            sleep(3)
            if alert_page.alert_title.is_displayed():
                common.take_screenshot('Background location popup')
                alert_page.confirm_button.click()

        sleep(5)

        with allure.step('New Earth weather service notification popup'):
            if alert_page.alert_img.is_displayed():
                common.take_screenshot('New Earth weather service notification')
                alert_page.next_button.click()

        with allure.step('Version update notification popup'):
            if alert_page.alert_card.is_displayed():
                common.take_screenshot('Version update notification')
                alert_page.close_button.click()

        with allure.step('Wait for the page to load to the home screen'):
            home_page.wait_for_page_to_load()
            common.take_screenshot('MyObservatory home page')

        with allure.step('Click the menu button'):
            common.wait_for_element(home_page.hamburger_button)
            home_page.hamburger_button.click()
            common.take_screenshot('Expand the menu')
        
        with allure.step('Click the "Forecast & Warning Services" button'):
            common.wait_for_element(home_page.forecast_and_warning_services_button)
            home_page.forecast_and_warning_services_button.click()
            common.take_screenshot('Expand the "Forecast & Warning Services"')

        with allure.step('Click the "9-Day Forecast" button and wait for the page to load'):
            common.wait_for_element(home_page.nine_day_forecast_button)
            home_page.nine_day_forecast_button.click()
            sleep(3)
            forecast_page.wait_for_page_to_load()
            common.take_screenshot('"9-Day Forecast" default page')

        with allure.step('Scroll to the 9th-day weather forecast'):
            today = datetime.now()
            nine_day = today + timedelta(days=8)
            nine_day_str = f'{nine_day.month}月{nine_day.day}日'

            for i in range(5):
                screen_size = driver.get_window_size()
                width = screen_size["width"] // 2
                start_y = screen_size["height"] * 0.8  # Screen bottom
                end_y = screen_size["height"] * 0.2  # Screen top
                driver.swipe(width, start_y, width, end_y, 800)               

            assert forecast_page.get_day_weather(nine_day_str).is_displayed()==True
            common.take_screenshot(f'The 9th-day weather forecast')
