from gcwebapp.Constants            import TT_Constants
from gcwebapp.BaseTestCase         import BaseTestCase
from gcwebapp.pages.LandingPage    import LandingPage
import unittest
import time
import nose

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
      	login_pro_object = LandingPage(self.driver)
      	login_pro_object.loginPro()
        
    
    def tearDown(self):
        super(logInPro, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



