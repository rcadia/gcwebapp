from gcwebapp.Constants                   import TT_Constants
from gcwebapp.BaseTestCase                import BaseTestCase
from gcwebapp.pages.LandingPage           import LandingPage
from gcwebapp.pages.ProHomePage           import ProHomePage
from gcwebapp.pages.ExerciseListPage      import ExerciseListPage
from gcwebapp.pages.ExerciseOverviewPage  import ExerciseOverviewPage            
import nose
import unittest
import time

"""
Scenario: Pro enters a Description to a newly created exercise.
Given I am pro
And I added a new exercise
And I click on new Exercise
And I am redirected to exercise overview
When I enter a description
And I click outside of the description area
Then the my input value is visible
"""


class addDescExercise(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(addDescExercise, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_addDescription(self):
        add_description_obj = LandingPage(self.driver)
        add_description_obj.loginPro()

        add_description_obj = ProHomePage(self.driver)
        add_description_obj.switchToExercises()

        add_description_obj = ExerciseListPage(self.driver)
        add_description_obj.switch_exerciseList()

        add_description_obj = ExerciseOverviewPage(self.driver)
        add_description_obj.addDescription()


    def tearDown(self):
        super(addDescExercise, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



