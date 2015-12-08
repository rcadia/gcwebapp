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

class WorkoutListPage(BasePage):

    def __init__(self, driver):
        super(WorkoutListPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10, "xpath", "//*[@class='gc-breadcrumbs-title']//*[.='Workouts']")
        except:
            raise IncorrectPageException

    def switch_WorkoutOverview(self):
        self.click(10, "xpath", "(//a[@class='gc-exercises-link'])[1]")
        self.wait_for_element_visibility(10, "xpath", "//region[@id='gc-privacy-button-region']")

    def addWorkout(self):
        mainWindowHandle  = self.driver.window_handles
        self.click(45, "xpath", "//a[@class='btn btn-link gc-show-add-exercise-modal']")
        allWindowsHandles = self.driver.window_handles
        for handle in allWindowsHandles:
          if handle != mainWindowHandle[0]:
            self.switch_to_window(handle)
            break
        randomNumber = randint(0001, 9999)
        WorkoutNameGenerate = "WORKOUT_" + str(randomNumber)
        self.fill_out_field("xpath", "//*[@id='gc-modal-region']//input[@class='form-control']", WorkoutNameGenerate)                    
        self.click(45, "xpath", "//*[@id='gc-modal-region']//button[@class='btn btn-primary gc-add-personal-best-add']")
        self.wait_for_element_visibility(10, "xpath", "//a[@class='gc-exercises-link'][contains(text(),'"+WorkoutNameGenerate+"')]") 

    def deleteWorkout(self):
        self.click(45, "xpath", "(//input[@type='checkbox'])[2]")
        WorkoutLocator = self.find_element("xpath", "(//a[@class='gc-exercises-link'])[1]").text
        mainWindowHandle = self.driver.window_handles
        self.click(45, "xpath", "//span[@class='fa fa-trash']")
        allWindowsHandles = self.driver.window_handles
        for handle in allWindowsHandles:
          if handle != mainWindowHandle[0]:
            self.switch_to_window(handle)
            break
        self.click(45, "xpath", "//button[@class='btn btn-danger confirm'][@data-dismiss='modal'][.='Delete']")
        time.sleep(2)
        WorkoutLocator2 = self.find_element("xpath", "(//a[@class='gc-exercises-link'])[1]").text
        assert WorkoutLocator != WorkoutLocator2