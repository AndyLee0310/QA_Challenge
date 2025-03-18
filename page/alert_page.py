from appium.webdriver.webdriver import By, WebDriver


class AlertPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def alert_title(self):
        """
        alert title
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/alertTitle')

    @property
    def alert_img(self):
        """
        alert image
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/img_view')
    
    @property
    def alert_card(self):
        """
        alert card
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/card')

    @property
    def next_button(self):
        """
        next button
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/exit_btn')
    
    @property
    def close_button(self):
        """
        close button
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/exit_btn')
    
    @property
    def confirm_button(self):
        """
        confirm button
        """
        return self.driver.find_element(By.ID, 'android:id/button1')
