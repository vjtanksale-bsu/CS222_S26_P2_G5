import unittest
from user_story_04 import is_empty_schedule
from user_story_04 import display_schedule

class TestUserStory04(unittest.TestCase):

    # Tests that an empty schedule is recognized
    def test_empty_schedule(self):
        schedule = []
        self.assertTrue(is_empty_schedule(schedule))

    # Tests that a schedule with courses is not empty
    def test_not_empty_schedule(self):
        schedule = [
            {
                "course": "CS120",
                "section": "001",
                "days": "MWF",
                "start": "0900",
                "end": "0950"
            }
        ]
        self.assertFalse(is_empty_schedule(schedule))

    # Tests displaying an empty schedule
    def test_display_empty_schedule(self):
        schedule = []
        result = display_schedule(schedule)
        self.assertEqual(result, "No schedule available")

    # Tests that the course number is displayed
    def test_display_course_number(self):
        schedule = [
            {
                "course": "CS120",
                "section": "001",
                "days": "MWF",
                "start": "0900",
                "end": "0950"
            }
        ]
        result = display_schedule(schedule)
        self.assertIn("CS120", result)

    # Tests that all course information is displayed
    def test_display_course_information(self):
        schedule = [
            {
                "course": "CS120",
                "section": "001",
                "days": "MWF",
                "start": "0900",
                "end": "0950"
            }
        ]
        result = display_schedule(schedule)
        self.assertIn("CS120", result)
        self.assertIn("001", result)
        self.assertIn("MWF", result)
        self.assertIn("0900", result)
        self.assertIn("0950", result)

    # Tests displaying multiple courses
    def test_display_multiple_courses(self):
        schedule = [
            {
                "course": "CS120",
                "section": "001",
                "days": "MWF",
                "start": "0900",
                "end": "0950"
            },
            {
                "course": "CS121",
                "section": "002",
                "days": "TR",
                "start": "1100",
                "end": "1150"
            }
        ]
        result = display_schedule(schedule)
        self.assertIn("CS120", result)
        self.assertIn("CS121", result)
        self.assertIn("001", result)
        self.assertIn("002", result)
        self.assertIn("MWF", result)
        self.assertIn("TR", result)
        self.assertIn("0900", result)
        self.assertIn("0950", result)
        self.assertIn("1100", result)
        self.assertIn("1150", result)


if __name__ == "__main__":
    unittest.main()
        