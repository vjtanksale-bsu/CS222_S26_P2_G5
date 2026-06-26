class ScheduleGenerator:
    def __init__(self, selected_courses):
        self.selected_courses = selected_courses
        self.checked_course_count = 0
        self.valid_schedule = True
        self.NO_SCHEDULE_MSG = "No valid schedule could be found. Please select different courses."

    def has_valid_schedule(self):
        self._check_all_course_conflicts()
        return self.valid_schedule

    def _check_all_course_conflicts(self):
        self.checked_course_count = len(self.selected_courses)
        for i in range(len(self.selected_courses)):
            course_a = self.selected_courses[i]
            for j in range(i + 1, len(self.selected_courses)):
                course_b = self.selected_courses[j]
                shared_days = set(course_a["days"]) & set(course_b["days"])
                if shared_days:
                    if not (course_a["end"] <= course_b["start"] or course_b["end"] <= course_a["start"]):
                        self.valid_schedule = False

    def generate_schedule(self):
        self._check_all_course_conflicts()
        if not self.valid_schedule:
            print(self.NO_SCHEDULE_MSG)
            return
        self._print_full_schedule()

    def _print_full_schedule(self):
        for course in self.selected_courses:
            print(f"Course Number: {course['num']}")
            print(f"Section: {course.get('section', 'N/A')}")
            print(f"Meeting Days: {course['days']}")
            print(f"Time: {course['start']}:00 - {course['end']}:00\n")
