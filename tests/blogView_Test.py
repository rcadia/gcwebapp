from gcwebapp.Constants            import TT_Constants
from gcwebapp.BaseTestCase         import BaseTestCase
from gcwebapp.Common               import Common
from gcwebapp.UIMap                import PublicPageMap
import unittest
import time

"""
Scenario: Pro user logs in using valid credentials.
Given I am a Pro
And I navigate to Public Page
When I click on Blog
Then I am redirected to Blog page
And I see the newsletter email.

"""


class blogView(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(blogView, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_blog(self):
        common_obj = Common(self.driver)

        common_obj.wait_for_element_visibility(10, 
                                               "xpath", 
                                               PublicPageMap["BlogButtonsXpath"]
        )
        common_obj.click(10, 
                        "xpath", 
                        PublicPageMap["BlogButtonsXpath"]
        )
        common_obj.wait_for_element_visibility(10, 
                                               "xpath", 
                                              PublicPageMap["NewsEmailfieldXpath"]
        )
    
    def tearDown(self):
        super(blogView, self).tearDown()
        

if __name__ == "__main__":
   unittest.main()



