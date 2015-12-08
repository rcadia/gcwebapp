from gcwebapp.Constants            import TT_Constants
from gcwebapp.BaseTestCase         import BaseTestCase
from random                        import randint                    
import nose
import unittest
import time
from gcwebapp.pages.LandingPage           import LandingPage
from gcwebapp.pages.ProHomePage           import ProHomePage
from gcwebapp.pages.WorkoutListPage       import WorkoutListPage
from gcwebapp.pages.WorkoutOverviewPage   import WorkoutOverviewPage 

"""
Scenario: Pro updates his workout name
Given I am pro
And I added a new workout
And I click on new workout
And I am redirected to workout overview
When I update the workout Name
And I click outside of the workout name area
Then I see it updated on (Sidebar, workout List and Overview)
"""


class updateWorkoutName(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(updateWorkoutName, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])

    def test_updateWorkoutName(self):
        update_WorkoutName = LandingPage(self.driver)
        update_WorkoutName.loginPro()

        update_WorkoutName = ProHomePage(self.driver)
        update_WorkoutName.switchToWorkouts()

        update_WorkoutName = WorkoutListPage(self.driver)
        update_WorkoutName.switch_WorkoutOverview()

        update_WorkoutName = WorkoutOverviewPage(self.driver)
        update_WorkoutName.updateWorkoutName()


        
    def tearDown(self):
        super(updateWorkoutName, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



