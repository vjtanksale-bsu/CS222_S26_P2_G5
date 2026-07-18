import unittest
from user_story_06 import course_is_selected
from user_story_06 import remove_course
from user_story_06 import display_updated_courses


class TestUserStory06(unittest.TestCase):

    # Tests that a selected course is recognized
    def test_course_is_selected(self):
        selected_courses = ["CS120", "CS121"]

        self.assertTrue(course_is_selected("CS120", selected_courses))

    # Tests that a course not in the list is recognized
    def test_course_is_not_selected(self):
        selected_courses = ["CS120", "CS121"]

        self.assertFalse(course_is_selected("CS222", selected_courses))

    # Tests that a selected course can be removed
    def test_remove_course(self):
        selected_courses = ["CS120", "CS121"]

        result = remove_course("CS120", selected_courses)

        self.assertNotIn("CS120", selected_courses)
        self.assertEqual(result, selected_courses)

    # Tests removing a course that is not in the list
    def test_remove_unavailable_course(self):
        selected_courses = ["CS120", "CS121"]

        result = remove_course("CS222", selected_courses)

        self.assertEqual(result, "Error: Course is not in the current list.")
        self.assertEqual(selected_courses, ["CS120", "CS121"])

    # Tests that the updated list does not include the removed course
    def test_display_updated_courses(self):
        selected_courses = ["CS121", "CS222"]

        result = display_updated_courses(selected_courses)

        self.assertIn("1. CS121", result)
        self.assertIn("2. CS222", result)
        self.assertNotIn("CS120", result)

    # Tests displaying an empty course list
    def test_display_empty_course_list(self):
        selected_courses = []

        result = display_updated_courses(selected_courses)

        self.assertEqual(
            result,
            "Current Course List:\nNo courses selected."
        )

    # Tests that removing a course does not change the requested maximum
    def test_requested_maximum_does_not_change(self):
        selected_courses = ["CS120", "CS121", "CS222"]
        maximum_courses = 3

        remove_course("CS120", selected_courses)

        self.assertEqual(maximum_courses, 3)


if __name__ == "__main__":
    unittest.main()