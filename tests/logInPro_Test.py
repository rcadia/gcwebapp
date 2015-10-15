from gcwebapp.Constants            import TT_Constants
from gcwebapp.BaseTestCase         import BaseTestCase
from gcwebapp.Common               import Common
from gcwebapp.UIMap                import PublicPageMap
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
                                               PublicPageMap["UsernameFieldXpath"]
        )
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
                        PublicPageMap["LoginButtonNameXpath"])

        common_obj.wait_for_element_visibility(10, 
                                               "xpath", 
                                               "//*[@id='logout-form']//div[@class='welcome-message']"
        )
        
        time.sleep(5)

    
    def tearDown(self):
        super(logInPro, self).tearDown()
        

if __name__ == "__main__":
   unittest.main()



