from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.select        import Select
from selenium.webdriver.support               import expected_conditions as EC
from selenium.webdriver.common.by             import By
from abc                                      import abstractmethod
from gcwebapp.Constants                       import LocatorMode
from BasePage                                 import BasePage
from random                                   import randint
from gcwebapp.pages.LandingPage               import LandingPage

class ExerciseListPage(BasePage):

    def __init__(self, driver):
        super(ExerciseListPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10, "xpath", "//*[@class='gc-breadcrumbs-title']//*[.='Exercises']")
        except:
            raise IncorrectPageException

    def addExercise(self):
        mainWindowHandle  = self.driver.window_handles
        self.click(45, "xpath", "//a[@class='btn btn-link gc-show-add-exercise-modal']")
        allWindowsHandles = self.driver.window_handles
        for handle in allWindowsHandles:
          if handle != mainWindowHandle[0]:
            self.switch_to_window(handle)
            break
        randomNumber = randint(0001, 9999)
        exerciseNameGenerate = "Exercise " + str(randomNumber)
        self.fill_out_field("xpath", "//*[@id='gc-modal-region']//input[@class='form-control']", exerciseNameGenerate)                    
        self.click(45, "xpath", "//*[@id='gc-modal-region']//button[@class='btn btn-primary gc-add-personal-best-add']")

      