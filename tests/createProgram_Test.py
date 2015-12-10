from gcwebapp.Constants            import TT_Constants
from gcwebapp.BaseTestCase         import BaseTestCase               
import unittest
import time
import nose
from gcwebapp.pages.LandingPage       import LandingPage
from gcwebapp.pages.ProHomePage       import ProHomePage
from gcwebapp.pages.ProgramListPage   import ProgramListPage

"""
Scenario: Pro creates a new program.
Given I am a Pro
And I am in program List
When I press Add program
And a modal pop up appears
And I enter an program name
Then see my program in program list 
And I see it in Sidebar

"""


class createProgram(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(createProgram, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_createProgram(self):
        create_program_obj = LandingPage(self.driver)
        create_program_obj.loginPro()

        create_program_obj = ProHomePage(self.driver)
        create_program_obj.switchToPrograms()

        create_program_obj = ProgramListPage(self.driver)
        create_program_obj.addProgram()

    def tearDown(self):
        super(createProgram, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



