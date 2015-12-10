from selenium                      import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from gcwebapp.Constants            import TT_Constants
from gcwebapp.BaseTestCase         import BaseTestCase
from random                        import randint                    
import unittest
import time
import nose
from gcwebapp.pages.LandingPage         import LandingPage
from gcwebapp.pages.ProHomePage         import ProHomePage
from gcwebapp.pages.ProgramListPage     import ProgramListPage

"""
Scenario: Pro deletes an existing program.
Given I am a Pro
And I am in program List
And I click on a random program item
When I press the trash-button
And I switch my focus to modal popup
And I click 'Delete' 
Then the program item is deleted
And I cannot see it in program list.

"""


class deleteProgram(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(deleteProgram, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_deleteProgram(self):
        delete_Program_obj = LandingPage(self.driver)
        delete_Program_obj.loginPro()

        delete_Program_obj = ProHomePage(self.driver)
        delete_Program_obj.switchToPrograms()

        delete_Program_obj = ProgramListPage(self.driver)
        delete_Program_obj.deleteProgram()

    def tearDown(self):
        super(deleteProgram, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



