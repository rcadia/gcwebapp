from gcwebapp.Constants                   import TT_Constants
from gcwebapp.BaseTestCase                import BaseTestCase
from gcwebapp.pages.LandingPage           import LandingPage
from gcwebapp.pages.ProHomePage           import ProHomePage
from gcwebapp.pages.ExerciseListPage      import ExerciseListPage
from gcwebapp.pages.ExerciseOverviewPage  import ExerciseOverviewPage            
import nose
import unittest
import time

"""
Scenario: Pro enters a Description to a newly created exercise.
Given I am pro
And I added a new exercise
And I click on new Exercise
And I am redirected to exercise overview
When I enter a description
And I click outside of the description area
Then the my input value is visible
"""


class addDescExercise(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(addDescExercise, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_createExercise(self):
        common_obj = Common(self.driver)

        common_obj.wait_for_element_visibility(45, 
                                               "xpath", 
                                               PublicPageMap["UsernameFieldXpath"]
        )
#Given I am a Pro
        common_obj.fill_out_field("xpath", 
                                  PublicPageMap["UsernameFieldXpath"],
                                  TT_Constants["proUsername"]                          
        )
        common_obj.fill_out_field("xpath", 
                                  PublicPageMap["PasswordFieldXpath"],
                                  TT_Constants["proPassword"]
        )
        common_obj.click(45, 
                        "xpath", 
                        PublicPageMap["LoginButtonNameXpath"]
        )
        common_obj.wait_for_element_visibility(45, 
                                               "xpath", 
                                               ProHomepage["GlobalSearchBarXpath"]
        )
#And I added a new exercise
        common_obj.click(45, 
                        "xpath", 
                        ProSidebar["ExercisesButtonLink"]
        )
        mainWindowHandle  = self.driver.window_handles
        common_obj.click(45, "xpath", ProHomepage["AddEWPButtonXpath"])
        allWindowsHandles = self.driver.window_handles
        for handle in allWindowsHandles:
          if handle != mainWindowHandle[0]:
            common_obj.switch_to_window(handle)
            break
        #exercise creation
        randomNumber         = randint(0001, 9999)
        exerciseNameGenerate = "Exercise ", randomNumber                 
        common_obj.fill_out_field("xpath",
                                  ModalPopupMap["AddExercisePopup"],
                                  exerciseNameGenerate
        )                    
        common_obj.click(45, 
                        "xpath", 
                        ModalPopupMap["AddExerciseButton"]
        )
        common_obj.wait_for_element_visibility(45, 
                                               "xpath", 
                                               "//a[contains(text(),"+str(randomNumber)+")][@class='gc-exercises-link']"
        )
#And I click on the new exercise
        common_obj.click(45, 
                        "xpath", 
                        "//a[contains(text(),"+str(randomNumber)+")][@class='gc-exercises-link']"
        )
#And I am redirected to exercise overview
        common_obj.wait_for_element_visibility(45, 
                                               "xpath", 
                                               "//span[.='Exercises']"
        )
#When I enter a description
        common_obj.wait_for_element_visibility(45, 
                                               "xpath", 
                                               ProHomepage["ExerciseDescField"]
        )

        common_obj.fill_out_field("xpath",
                                  ProHomepage["ExerciseDescField"],
                                  "This is an auto generated text created for WebApp Testing...!"
        )  
#And I click outside of the description area
        common_obj.click(45, 
                        "xpath", 
                        "//div [@class='gc-topbar-search']"
        )
#Then the my input value is visible
        VerifyValue = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_xpath(ProHomepage["ExerciseDescField"])).get_attribute("value")
        assert "This is an auto generated text created for WebApp Testing...!" == VerifyValue

    def tearDown(self):
        super(addDescExercise, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



