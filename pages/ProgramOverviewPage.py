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

class ProgramOverviewPage(BasePage):

    def __init__(self, driver):
        super(ProgramOverviewPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(45, "xpath", "//region[@id='gc-privacy-button-region']")
        except:
            raise IncorrectPageException

    def addDescription(self):
    	random = randint(1,100)
    	self.click(45, "xpath", "//*[@class='gc-program-description-editor gc-description-editor form-control']")
    	self.fill_out_field("xpath", "//*[@class='gc-program-description-editor gc-description-editor form-control']", "This is an automated note input by Ross for testing purposes "+ str(random)+".")
    	self.click(45, "xpath", "//div [@class='gc-topbar-search']")  
    	self.wait_for_element_visibility(45, "xpath", "//div[@class='gc-notify-inner gc-notify-inner-success messenger-will-hide-after']")
    	ProgramDescription = self.find_element("xpath", "//*[@class='gc-program-description-editor gc-description-editor form-control']").get_attribute("value")
    	assert "This is an automated note input by Ross for testing purposes "+ str(random)+"." == ProgramDescription

    def updateWorkoutName(self):
        random = randint(0,9999)
        PrgoramName = self.wait_for_element_visibility(45, "xpath", "//span[@contenteditable='true']").text
        ProgramRenamed = PrgoramName[0:8]+"_"+str(random)
        self.click(45, "xpath", "//span[@contenteditable='true']")
        self.fill_out_field("xpath", "//span[@contenteditable='true']", ProgramRenamed)
        self.click(45, "xpath", "//div [@class='gc-topbar-search']")
        self.wait_for_element_visibility(45, "xpath", "//div[@class='gc-notify-inner gc-notify-inner-success messenger-will-hide-after']")
        self.click(45, "xpath", "//region[@data-name='workout_templates']//*[@class='gc-menu-item-arrow toggle-it']")
        self.wait_for_element_visibility(45, "xpath", "//*[@class='col-xs-10 gc-sidebar-folder-name'][contains(text(), '"+ProgramRenamed+"')]")
        self.click(45, "xpath", "//*[@class='col-xs-8 gc-sidebar-cat-name'][.='PROGRAMS']")
        self.wait_for_element_visibility(45, "xpath", "//*[@class='gc-exercises-link'][contains(text(), '"+ProgramRenamed+"')]")

