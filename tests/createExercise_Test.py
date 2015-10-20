from gcwebapp.Constants            import TT_Constants
from gcwebapp.BaseTestCase         import BaseTestCase
from gcwebapp.Common               import Common
from gcwebapp.UIMap                import PublicPageMap
from gcwebapp.UIMap                import ProHomepage
from gcwebapp.UIMap                import ProSidebar
from gcwebapp.UIMap                import ModalPopupMap
from random                        import randint                    
import unittest
import time

"""
Scenario: Pro creates a new exercise.
Given I am a Pro
And I am in Exercise List
When I press Add Exercise
And a modal pop up appears
And I enter an exercise name
Then see my exercise in Exercise list 
And I see it in Sidebar

"""


class logInPro(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(logInPro, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_LogInPro(self):
        common_obj = Common(self.driver)

        common_obj.wait_for_element_visibility(10, 
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
        common_obj.click(10, 
                        "xpath", 
                        PublicPageMap["LoginButtonNameXpath"]
        )
        common_obj.wait_for_element_visibility(20, 
                                               "xpath", 
                                               ProHomepage["GlobalSearchBarXpath"]
        )
#And I am in Exercise List
        common_obj.click(10, 
                        "xpath", 
                        ProSidebar["ExercisesButtonLink"]
        )
#When I press Add Exercise       
#And A modal pop up appears
        mainWindowHandle  = self.driver.window_handles
        common_obj.click(10, "xpath", ProHomepage["AddExerciseButtonXpath"])
        allWindowsHandles = self.driver.window_handles
        for handle in allWindowsHandles:
          if handle != mainWindowHandle[0]:
            common_obj.switch_to_window(handle)
            break
#And I enter an exercise name 
        randomNumber         = randint(0001, 9999)
        exerciseNameGenerate = "Exercise ", randomNumber                 
        common_obj.fill_out_field("xpath",
                                  ModalPopupMap["AddExercisePopup"],
                                  exerciseNameGenerate
        )                    
        common_obj.click(10, 
                        "xpath", 
                        ModalPopupMap["AddExerciseButton"]
        )
#Then see my exercise in Exercise list
        common_obj.wait_for_element_visibility(10, 
                                               "xpath", 
                                               "//a[contains(text(),"+str(randomNumber)+")][@class='gc-exercises-link']"
        )
#And I see it in Sidebar
        common_obj.find_element("xpath", 
                                "//span[contains(text(),"+str(randomNumber)+")]"
        )

    def tearDown(self):
        super(logInPro, self).tearDown()
        

if __name__ == "__main__":
   unittest.main()



