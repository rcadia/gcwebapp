from gcwebapp.Constants                 import TT_Constants
from gcwebapp.BaseTestCase              import BaseTestCase
from random                             import randint
import unittest
import nose
from gcwebapp.pages.LandingPage         import LandingPage
from gcwebapp.pages.ProHomePage         import ProHomePage
from gcwebapp.pages.WorkoutListPage     import WorkoutListPage

"""
Scenario: Pro deletes an existing workout.
Given I am a Pro
And I am in workout List
And I click on a random workout item
When I press the trash-button
And I switch my focus to modal popup
And I click 'Delete' 
Then the workout item is deleted
And I cannot see it in workout list.

"""


class deleteWorkout(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(deleteWorkout, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_deleteWorkout(self):
        
        delete_workout_obj = LandingPage(self.driver)
        delete_workout_obj.loginPro()

        delete_workout_obj = ProHomePage(self.driver)
        delete_workout_obj.switchToWorkouts()

        delete_workout_obj = WorkoutListPage(self.driver)
        delete_workout_obj.deleteWorkout()

    def tearDown(self):
        super(deleteWorkout, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



