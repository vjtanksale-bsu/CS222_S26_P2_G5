import unittest
from user_story_03 import is_valid_course
from user_story_03 import is_duplicate_course
from user_story_03 import add_course

class TestUserStory03(unittest.TestCase):

    # Test that a valid course is found
    def test_valid_course(self):
        available_courses = ["CS120", "CS121", "CS222"]
        self.assertTrue(is_valid_course("CS120", available_courses))

    # Test that an invalid course is not found
    def test_invalid_course(self):
        available_courses = ["CS120", "CS121", "CS222"]
        self.assertFalse(is_valid_course("MA165", available_courses))
    
    # Tests that duplicate courses is recognized
    def test_duplicate_course(self):
        selected_courses = ["CS120"]
        self.assertTrue(is_duplicate_course("CS120", selected_courses))

    # Tests that new course is not duplicate
    def test_not_duplicate_course(self):
        selected_courses = ["CS120"]
        self.assertFalse(is_duplicate_course("CS121", selected_courses))

    # Test that valid course can be added
    def test_add_valid_course(self):
        available_courses = ["CS120", "CS121", "CS222"]
        selected_courses = []

        result = add_course("CS120", available_courses, selected_courses)

        self.assertTrue(result)
        self.assertIn("CS120", selected_courses)
    
    # Test that adding invalid course fails
    def test_add_invalid_course(self):
        available_courses = ["CS120", "CS121", "CS222"]
        selected_courses = []

        result = add_course("MA165", available_courses, selected_courses)

        self.assertFalse(result)

    # Tests adding the same course twice fails
    def test_add_duplicate_course(self):
        available_courses = ["CS120", "CS121", "CS222"]
        selected_courses = ["CS120"]

        result = add_course("CS120", available_courses, selected_courses)

        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()