from GCwebapp.Constants            import TT_Constants
from GCwebapp.BaseTestCase         import BaseTestCase
from GCwebapp.Common               import Common
from GCwebapp.UIMap                import LandingPageMap
import unittest
import time

"""
Scenario: Pro user logs in using valid credentials.
"""


class logInPro(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(logInPro, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_SendRequestTest(self):
        common_obj = Common(self.driver)

        common_obj.wait_for_element_visibility(10, 
                                               "xpath", 
                                               "//input[@id='username']"
        )
        common_obj.fill_out_field("xpath", 
                                  LandingPageMap["UsernameFieldXpath"],
                                  TT_Constants["Cust_Username"]                          
        )
        common_obj.fill_out_field("xpath", 
                                  LandingPageMap["PasswordFieldXpath"],
                                  TT_Constants["Cust_Password"]
        )
        common_obj.click(10, "xpath", "//button[@class='btn sidoBtn btn-default btn-success HeadBtn']")

        common_obj.wait_for_element_visibility(10, 
                                               "xpath", 
                                               "//*[@id='logout-form']//div[@class='welcome-message']"
        )
        
        time.sleep(5)

    
    def tearDown(self):
        super(logInPro, self).tearDown()
        

if __name__ == "__main__":
   unittest.main()



