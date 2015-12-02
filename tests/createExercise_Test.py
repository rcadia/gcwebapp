from gcwebapp.Constants                 import TT_Constants
from gcwebapp.BaseTestCase              import BaseTestCase
from random                             import randint
import unittest
import nose
from gcwebapp.pages.LandingPage			import LandingPage
from gcwebapp.pages.ProHomePage    		import ProHomePage
from gcwebapp.pages.ExerciseListPage    import ExerciseListPage
                    

"""
Scenario: Pro creates a new exercise.
Given I am a Pro
And I am in Exercise List
When I press Add Exercise
And a modal pop up appears
And I enter an exercise name
Then see my exercise in Exercise list 
And I see it in Sidebar

"""


class createExercise(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(createExercise, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    def test_AddExercise(self):
    	create_exercise_obj = LandingPage(self.driver)
        create_exercise_obj.loginPro()

        create_exercise_obj = ProHomePage(self.driver)
        create_exercise_obj.switchToExercises()

        create_exercise_obj = ExerciseListPage(self.driver)
        create_exercise_obj.addExercise()

    def tearDown(self):
        super(createExercise, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



