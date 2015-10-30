from gcwebapp.Constants            import TT_Constants
from selenium                      import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from gcwebapp.BaseTestCase         import BaseTestCase
from gcwebapp.Common               import Common
from gcwebapp.UIMap                import PublicPageMap
from gcwebapp.UIMap                import ProHomepage
from gcwebapp.UIMap                import ProSidebar
from gcwebapp.UIMap                import ModalPopupMap
from random                        import randint                    
import nose
import unittest
import time

"""
Scenario: Pro updates his exercise name
Given I am pro
And I added a new exercise
And I click on new Exercise
And I am redirected to exercise overview
When I update the Exercise Name
And I click outside of the Exercise name area
Then I see it updated on (Sidebar, Exercise List and Overview)
"""


class updateExerciseName(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(updateExerciseName, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_updateExerciseName(self):
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
        exerciseNameGenerate = ("Exercise ",randomNumber)                
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
        #get data-id of the newly created exercise
        DataID = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_xpath("//a[contains(text(),"+str(randomNumber)+")][@class='gc-exercises-link']")).get_attribute("data-key")
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
#When I update the Exercise Name
        common_obj.wait_for_element_visibility(45, 
                                               "xpath", 
                                               ProHomepage["EWPnameField"]
        )
        renamedExercise = (exerciseNameGenerate, "_1") 
        common_obj.fill_out_field("xpath",
                                  ProHomepage["EWPnameField"],
                                  renamedExercise
        )  
#And I click outside of the Exercise name area
        common_obj.click(45, 
                        "xpath", 
                        "//div [@class='gc-topbar-search']"
        )
#Then the my input value is visible: Sidebar
        common_obj.click(45, 
                        "xpath", 
                        ProSidebar["ExerciseDropdown"]
        )
        SideBarExerciseAfter  = "//span[@class='col-xs-10 gc-sidebar-folder-name'][@data-key="+DataID+"][contains(text(),'_1')]"
        common_obj.find_element("xpath", 
                                SideBarExerciseAfter
        )
#Then the my input value is visible: Exercise List
        #Click the exercise sidebar
        common_obj.click(45, 
                        "xpath", 
                        ProSidebar["ExercisesButtonLink"]
        )
        ListExerciseAfter  = "//a[@class='gc-exercises-link'][@data-key="+DataID+"][contains(text(),'_1')]"

        common_obj.find_element("xpath", 
                                ListExerciseAfter
        )

    def tearDown(self):
        super(updateExerciseName, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



