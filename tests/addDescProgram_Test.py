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
Scenario: Pro enters a Description to a newly created Program.
Given I am pro
And I added a new Program
And I click on new Program
And I am redirected to Program overview
When I enter a description
And I click outside of the description area
Then the my input value is visible
"""


class addDescProgram(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(addDescProgram, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_addDescProgram(self):
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
#And I added a new Program
        #And I am in Program List
        common_obj.click(45, 
                        "xpath", 
                        ProSidebar["ProgramButtonLink"]
        )
        #When I press Add Program       
        #And A modal pop up appears
        mainWindowHandle  = self.driver.window_handles
        common_obj.click(45, "xpath", ProHomepage["AddEWPButtonXpath"])
        allWindowsHandles = self.driver.window_handles
        for handle in allWindowsHandles:
          if handle != mainWindowHandle[0]:
            common_obj.switch_to_window(handle)
            break
        #And I enter an Program name 
        randomNumber         = randint(0001, 9999)
        exerciseNameGenerate = "Program ", randomNumber                 
        common_obj.fill_out_field("xpath",
                                  ModalPopupMap["AddExercisePopup"],
                                  exerciseNameGenerate
        )                    
        common_obj.click(45, 
                        "xpath", 
                        ModalPopupMap["AddExerciseButton"]
        )
        #Then see my workout in Program list
        common_obj.wait_for_element_visibility(45, 
                                               "xpath", 
                                               "//a[contains(text(),"+str(randomNumber)+")][@class='gc-exercises-link']"
        )
#And I click on the new Program
        common_obj.click(45, 
                        "xpath", 
                        "//a[contains(text(),"+str(randomNumber)+")][@class='gc-exercises-link']"
        )
#And I am redirected to Program overview
        common_obj.wait_for_element_visibility(45, 
                                               "xpath", 
                                               "//span[.='Programs']"
        )
#When I enter a description
        common_obj.wait_for_element_visibility(45, 
                                               "xpath", 
                                               ProHomepage["ProgramDescField"]
        )

        common_obj.fill_out_field("xpath",
                                  ProHomepage["ProgramDescField"],
                                  "This is an auto generated text created for WebApp Testing...!"
        )  
#And I click outside of the description area
        common_obj.click(45, 
                        "xpath", 
                        "//div [@class='gc-topbar-search']"
        )
#Then the my input value is visible
        VerifyValue = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_xpath(ProHomepage["ProgramDescField"])).get_attribute("value")
        assert "This is an auto generated text created for WebApp Testing...!" == VerifyValue

        time.sleep(5)

    def tearDown(self):
        super(addDescProgram, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



