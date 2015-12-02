from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.select        import Select
from selenium.webdriver.support               import expected_conditions as EC
from selenium.webdriver.common.by             import By
from abc                                      import abstractmethod
from gcwebapp.Constants                       import LocatorMode
from BasePage                                 import BasePage

class ProHomePage(BasePage):

    def __init__(self, driver):
        super(ProHomePage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10, "xpath", "//input[@id='gc-topnav-search']")
        except:
            raise IncorrectPageException

    def switchToExercises(self):
        self.click(10, "xpath", "//span[.='EXERCISES']")
        self.wait_for_element_visibility(10, "xpath", "//*[@class='gc-breadcrumbs-title']//*[.='Exercises']")
        

      