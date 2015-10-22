from selenium                      import webdriver
from selenium.webdriver.support.ui import WebDriverWait
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
Scenario: Pro deletes an existing exercise.
Given I am a Pro
And I am in Exercise List
And I click on a random Exercise item
When I press the trash-button
And I switch my focus to modal popup
And I click 'Delete' 
Then the exercise item is deleted
And I cannot see it in exercise list.

"""


class deleteExercise(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(deleteExercise, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_deleteExercise(self):
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
#And I am in Exercise List
        common_obj.click(45, 
                        "xpath", 
                        ProSidebar["ExercisesButtonLink"]
        )
#And I click on a random Exercise item
        common_obj.click(45, 
                        "xpath", 
                        ProHomepage["ExerciseFirstRadioBtn"]
        )
        #get unique data-id of checkbox
        DataId = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_xpath(ProHomepage["ExerciseFirstRadioBtn"]))
        dataID2 = DataId.get_attribute("data-id")
        print dataID2
#When I press the trash-button
        mainWindowHandle  = self.driver.window_handles
        common_obj.click(45, 
                        "xpath", 
                        ProHomepage["EWPDeleteButton"]
        )
#And I switch my focus to modal popup
        allWindowsHandles = self.driver.window_handles
        for handle in allWindowsHandles:
          if handle != mainWindowHandle[0]:
            common_obj.switch_to_window(handle)
            break
#And I click 'Delete' 
        common_obj.click(45, 
                        "xpath", 
                        ModalPopupMap["Deletebutton"]
        )
        time.sleep(2)      
        #assert that the dataid is deleted.
        DataId = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_xpath(ProHomepage["ExerciseFirstRadioBtn"]))
        dataID3 = DataId.get_attribute("data-id")
        print dataID3

        assert dataID2 =! dataID3

    def tearDown(self):
        super(deleteExercise, self).tearDown()
        

if __name__ == "__main__":
   unittest.main()



