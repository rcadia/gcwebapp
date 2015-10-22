from gcwebapp.Constants            import TT_Constants
from gcwebapp.BaseTestCase         import BaseTestCase
from gcwebapp.Common               import Common
from gcwebapp.UIMap                import PublicPageMap
from gcwebapp.UIMap                import ProHomepage
import unittest
import time

"""
Scenario: Pro user logs in using valid credentials.
Given I am a Pro
And I navigate to Public Page
When I enter valid credentials
Then I am redirected to homepage
And I see the global search bar 

"""


class logInPro(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(logInPro, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_LogInPro(self):
        common_obj = Common(self.driver)

        common_obj.wait_for_element_visibility(50, 
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
        common_obj.click(50, 
                        "xpath", 
                        PublicPageMap["LoginButtonNameXpath"]
        )
        common_obj.wait_for_element_visibility(20, 
                                               "xpath", 
                                               ProHomepage["GlobalSearchBarXpath"]
        )

    
    def tearDown(self):
        super(logInPro, self).tearDown()
        

if __name__ == "__main__":
   unittest.main()



