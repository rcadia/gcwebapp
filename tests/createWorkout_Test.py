from gcwebapp.Constants            import TT_Constants
from gcwebapp.BaseTestCase         import BaseTestCase
from random                        import randint                    
import unittest
import time
import nose
from gcwebapp.pages.LandingPage     import LandingPage
from gcwebapp.pages.ProHomePage     import ProHomePage
from gcwebapp.pages.WorkoutListPage import WorkoutListPage

"""
Scenario: Pro creates a new Workout.
Given I am a Pro
And I am in Workout List
When I press Add Workout
And a modal pop up appears
And I enter an Workout name
Then see my Workout in Workout list 
And I see it in Sidebar

"""


class createWorkout(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(createWorkout, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_createWorkout(self):

        create_workout_obj = LandingPage(self.driver)
        create_workout_obj.loginPro()

        create_workout_obj = ProHomePage(self.driver)
        create_workout_obj.switchToWorkouts()

        create_workout_obj = WorkoutListPage(self.driver)
        create_workout_obj.addWorkout()

    def tearDown(self):
        super(createWorkout, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



