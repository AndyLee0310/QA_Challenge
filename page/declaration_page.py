from module.common import Common
from appium.webdriver.webdriver import By, WebDriver


class DeclarationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.common = Common(driver)

    def wait_for_page_to_load(self):
        """
        Wait for the page elements to appear, indicating that the page has fully loaded
        """
        self.common.wait_for_element(self.page_title)
        self.common.wait_for_element(self.page_content)
        self.common.wait_for_element(self.agree_button)

    @property
    def page_title(self):
        """
        statement title
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/txt_title')
    
    @property
    def page_content(self):
        """
        statement title
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/txt_content')

    @property
    def agree_button(self):
        """
        agree button
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/btn_agree')
    
    @property
    def disagree_button(self):
        """
        disagree button
        """
        return self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/btn_not_agree')
