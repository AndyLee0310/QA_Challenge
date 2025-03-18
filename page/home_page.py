from module.common import Common
from appium.webdriver.webdriver import By, WebDriver


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.common = Common(driver)

    def wait_for_page_to_load(self):
        """
        Wait for the page elements to appear, indicating that the page has fully loaded
        """
        self.common.wait_for_element(self.page_title)
        self.common.wait_for_element(self.current_date)
        self.common.wait_for_element(self.current_time)
        self.common.wait_for_element(self.current_location)

    @property
    def page_title(self):
        """
        page title_MyObservatory
        """
        return self.driver.find_element(By.XPATH, '//*[@text="我的天文台"]')

    @property
    def current_date(self):
        """
        current date
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/date')

    @property
    def current_time(self):
        """
        current time
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/time')
    
    @property
    def current_location(self):
        """
        current location
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/locationName')
    
    @property
    def hamburger_button(self):
        """
        Menu button
        """
        return self.driver.find_element(By.XPATH, '//*[@content-desc="向上瀏覽"]')
    
    @property
    def forecast_and_warning_services_button(self):
        """
        Forecast & Warning Services button
        """
        return self.driver.find_element(By.XPATH, '//*[contains(@text, "預報及警告服務")]')

    @property
    def nine_day_forecast_button(self):
        """
        9-Day Forecast
        """
        return self.driver.find_element(By.XPATH, '//*[@text="預報及警告服務"]/parent::*/parent::*/parent::*/following-sibling::*//*[contains(@text, "九天預報")]')
