from gcwebapp.Constants                 import TT_Constants
from gcwebapp.BaseTestCase              import BaseTestCase
from random                             import randint
import unittest
import nose
from gcwebapp.pages.LandingPage         import LandingPage
from gcwebapp.pages.ProHomePage         import ProHomePage
from gcwebapp.pages.ExerciseListPage    import ExerciseListPage
                    

class deleteExercises(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(deleteExercises, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    def test_deleteExercise(self):
        create_exercise_obj = LandingPage(self.driver)
        create_exercise_obj.loginPro()

        create_exercise_obj = ProHomePage(self.driver)
        create_exercise_obj.switchToExercises()

        create_exercise_obj = ExerciseListPage(self.driver)
        create_exercise_obj.deleteExercise()

    def tearDown(self):
        super(deleteExercises, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



