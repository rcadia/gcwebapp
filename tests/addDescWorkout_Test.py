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
Scenario: Pro enters a Description to a newly created Workout.
Given I am pro
And I added a new Workout
And I click on new Workout
And I am redirected to Workout overview
When I enter a description
And I click outside of the description area
Then the my input value is visible
"""


class addDescWorkout(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(addDescWorkout, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_AddDescriptionWorkout(self):

        add_description_obj = LandingPage(self.driver)
        add_description_obj.loginPro()

        add_description_obj = ProHomePage(self.driver)
        add_description_obj.switchToWorkouts()

        add_description_obj = WorkoutListPage(self.driver)
        add_description_obj.switch_WorkoutOverview()

        add_description_obj = WorkoutOverviewPage(self.driver)
        add_description_obj.addDescription()


    def tearDown(self):
        super(addDescWorkout, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



