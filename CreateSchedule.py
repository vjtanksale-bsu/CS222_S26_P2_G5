from CourseNumbers import ViewCourses
class ScheduleCreate():
    def __init__(self):
        self.schedule = {}

    def ScheduleList(self):
        try:
            a = int(input("Enter the amount of classes to add: "))
            self.schedule = {f"Class{i}": "empty" for i in range(1, a + 1)}
            self.printSchedule()
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")

    def printSchedule(self):
        print("----Schedule----")
        for key, value in self.schedule.items():
            if value == "empty":
                print(f"{key} : empty")
            else:
                print(f"{key} : {value['num']} ({value['section']}) | {value['days']} | {value['start']}-{value['end']}")

    def AddToSchedule(self, possible_courses):
        if not possible_courses:
            print("Error: No available courses found.")
            return

        b = input("Enter section number: ").strip()

        matched = [c for c in possible_courses if c["section"].strip() == b]

        if not matched:
            print(f"Error: Section {b} is not a valid section option.")
            return

        selected_course = matched[0]

        try:
            c = int(input("Where in your schedule would you like to put it?: "))
            key_spot = f"Class{c}"

            if key_spot in self.schedule:
                self.schedule[key_spot] = selected_course
                self.printSchedule()
            else:
                print("That is not a spot in the schedule")
        except ValueError:
            print("Invalid input. Please enter a valid slot number.")

    def RemoveFromSchedule(self):
        b = input("What class would you like to remove? ").upper().strip()
        remove_value = [key for key, value in self.schedule.items() if value.upper().strip() == b]

        if remove_value:
            for key in remove_value:
                self.schedule[key] = "empty"
            self.printSchedule()
        else:
            print("That class cannot be found")

    def manageSchedule(self, possible_courses):
        while True:
            total_slots = len(self.schedule)
            empty_slots = list(self.schedule.values()).count("empty")
            filled_slots = total_slots - empty_slots

            print(f"\nSlots: {filled_slots}/{total_slots} filled.")
            action = input("Type 'ADD' to add, 'REMOVE' to remove,'COURSES' to view available courses, or 'STOP' to exit: ").upper().strip()

            if action == "STOP":
                print("Exiting schedule manager loop.")
                break

            elif action == "ADD":
                self.AddToSchedule(possible_courses)

            elif action == "REMOVE":
                self.RemoveFromSchedule()

            elif action == "COURSES":
                if possible_courses:
                    for course in possible_courses:
                        print(f"{course['num']} ({course['section']}) | {course['days']} | {course['start']}-{course['end']}")

            else:
                print("Invalid action. Please enter ADD, REMOVE, or STOP.")

    def get_formatted_list(self):
        formatted_list = []
        for slot, course_data in self.schedule.items():
            if course_data != "empty":
                formatted_list.append({
                    "course": course_data["num"],
                    "course_num": course_data["num"],
                    "section": course_data["section"],
                    "days": course_data["days"],
                    "meeting_days": course_data["days"],
                    "start": course_data["start"],
                    "start_time": course_data["start"],
                    "end": course_data["end"],
                    "end_time": course_data["end"]
                })
        return formatted_list
            self.printSchedule()
        else:
            print("That class cannot be found")
