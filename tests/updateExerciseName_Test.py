from gcwebapp.Constants            import TT_Constants
from selenium.webdriver.support.ui import WebDriverWait
from gcwebapp.BaseTestCase         import BaseTestCase
from random                        import randint                    
import nose
import unittest
import time
from gcwebapp.pages.LandingPage           import LandingPage
from gcwebapp.pages.ProHomePage           import ProHomePage
from gcwebapp.pages.ExerciseListPage      import ExerciseListPage
from gcwebapp.pages.ExerciseOverviewPage  import ExerciseOverviewPage   

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
        update_ExcerciseName = LandingPage(self.driver)
        update_ExcerciseName.loginPro()

        update_ExcerciseName = ProHomePage(self.driver)
        update_ExcerciseName.switchToExercises()

        update_ExcerciseName = ExerciseListPage(self.driver)
        update_ExcerciseName.switch_exerciseList()

        update_ExcerciseName = ExerciseOverviewPage(self.driver)
        update_ExcerciseName.updateExerciseName()

    def tearDown(self):
        super(updateExerciseName, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



