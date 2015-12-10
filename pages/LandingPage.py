from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.select        import Select
from selenium.webdriver.support               import expected_conditions as EC
from selenium.webdriver.common.by             import By
from abc                                      import abstractmethod
from gcwebapp.Constants                       import LocatorMode
from BasePage                                 import BasePage

class LandingPage(BasePage):

    def __init__(self, driver):
        super(LandingPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(45, "xpath", "//button[.='Log in']")
        except:
            raise IncorrectPageException

    def loginPro(self):
        self.fill_out_field("xpath", "//input[@name='username']", "proautomate@yopmail.com")
        self.fill_out_field("xpath", "//input[@name='password']", "gymcloud")
        self.click(45, "xpath", "//button[.='Log in']")
        self.wait_for_element_visibility(45, "xpath", "//input[@id='gc-topnav-search']")

      