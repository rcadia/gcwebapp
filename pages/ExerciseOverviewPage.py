from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.select        import Select
from selenium.webdriver.support               import expected_conditions as EC
from selenium.webdriver.common.by             import By
from abc                                      import abstractmethod
from gcwebapp.Constants                       import LocatorMode
from random                                   import randint
from BasePage                                 import BasePage
import time

class ExerciseOverviewPage(BasePage):

    def __init__(self, driver):
        super(ExerciseOverviewPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10, "xpath", "//region[@id='gc-privacy-button-region']")
        except:
            raise IncorrectPageException
    def addDescription(self):
    	random = randint(1,100)
    	self.click(45, "xpath", "//textarea[@class='gc-exercise-description-editor form-control']")
    	self.fill_out_field("xpath", "//textarea[@class='gc-exercise-description-editor form-control']", "This is an automated note input by Ross for testing purposes "+ str(random)+".")
    	self.click(45, "xpath", "//div [@class='gc-topbar-search']")  
    	self.wait_for_element_visibility(10, "xpath", "//div[@class='gc-notify-inner gc-notify-inner-success messenger-will-hide-after']")
    	ExerciseDescription = self.find_element("xpath", "//textarea[@class='gc-exercise-description-editor form-control']").get_attribute("value")
    	assert "This is an automated note input by Ross for testing purposes "+ str(random)+"." == ExerciseDescription
