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
import string

class WorkoutOverviewPage(BasePage):

    def __init__(self, driver):
        super(WorkoutOverviewPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10, "xpath", "//region[@id='gc-privacy-button-region']")
        except:
            raise IncorrectPageException

    def addDescription(self):
    	random = randint(1,100)
    	self.click(45, "xpath", "//textarea[@class='gc-workout-description-editor gc-description-editor form-control']")
    	self.fill_out_field("xpath", "//textarea[@class='gc-workout-description-editor gc-description-editor form-control']", "This is an automated note input by Ross for testing purposes "+ str(random)+".")
    	self.click(45, "xpath", "//div [@class='gc-topbar-search']")  
    	self.wait_for_element_visibility(10, "xpath", "//div[@class='gc-notify-inner gc-notify-inner-success messenger-will-hide-after']")
    	WorkoutDescription = self.find_element("xpath", "//textarea[@class='gc-workout-description-editor gc-description-editor form-control']").get_attribute("value")
    	assert "This is an automated note input by Ross for testing purposes "+ str(random)+"." == WorkoutDescription

    def updateWorkoutName(self):
        random = randint(0,9999)
        WorkoutName = self.wait_for_element_visibility(10, "xpath", "//span[@contenteditable='true']").text
        WorkoutRenamed = WorkoutName[0:8]+"_"+str(random)
        self.click(10, "xpath", "//span[@contenteditable='true']")
        self.fill_out_field("xpath", "//span[@contenteditable='true']", WorkoutRenamed)
        self.click(45, "xpath", "//div [@class='gc-topbar-search']")
        self.wait_for_element_visibility(10, "xpath", "//div[@class='gc-notify-inner gc-notify-inner-success messenger-will-hide-after']")
        self.click(10, "xpath", "//region[@data-name='workout_templates']//*[@class='gc-menu-item-arrow toggle-it']")
        self.wait_for_element_visibility(10, "xpath", "//*[@class='col-xs-10 gc-sidebar-folder-name'][contains(text(), '"+WorkoutRenamed+"')]")
        self.click(10, "xpath", "//*[@class='col-xs-8 gc-sidebar-cat-name'][.='WORKOUTS']")
        self.wait_for_element_visibility(10, "xpath", "//*[@class='gc-exercises-link'][contains(text(), '"+WorkoutRenamed+"')]")

