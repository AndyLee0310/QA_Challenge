from module.common import Common
from appium.webdriver.webdriver import By, WebDriver


class ForecastPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.common = Common(driver)

    def wait_for_page_to_load(self):
        """
        Wait for the page elements to appear, indicating that the page has fully loaded
        """
        self.common.wait_for_element(self.page_title)
        self.common.wait_for_element(self.main_forecast_content)

    @property
    def page_title(self):
        """
        page title_Weather Forecast
        """
        return self.driver.find_element(By.XPATH, '//*[@text="天氣預報"]')

    @property
    def main_forecast_content(self):
        """
        Main Weather Forecast Content
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/mainAppSevenDayGenSit')
    
    def get_day_weather(self, day):
        """
        Retrieve the weather information for the specified date
        """
        day_weather = self.driver.find_element(By.XPATH, f'//*[@text="{day}"]')
        return day_weather
