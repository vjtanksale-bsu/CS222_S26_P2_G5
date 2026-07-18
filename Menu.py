import schedule_generator
from CourseNumbers import ViewCourses
from CreateSchedule import ScheduleCreate
from user_story_04 import is_empty_schedule, display_schedule

def mainMenu():
    courses = ViewCourses()
    create = ScheduleCreate()

    while(True):
        print("----Menu Options----",
              "\n1.) View Available Courses",
              "\n2.) Create Schedule",
              "\n3.) View Schedule",
              "\n4.) Quit")
        try:
            i = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")
            continue


        if i == 1:
            available_list = courses.viewCourses()
            print("\n--- Available System Courses ---")

        elif i == 2:
            create.ScheduleList()
            create.printSchedule()
            available_list = courses.viewCourses()
            create.manageSchedule(available_list)


        elif i == 3:
            if is_empty_schedule(create.schedule):
                print("No schedule to show")
            else:
                formatted_schedule = create.get_formatted_list()
                print(display_schedule(formatted_schedule))

        elif i == 4:
            if not is_empty_schedule(create.schedule):
                save_choice = input("\nWould you like to save your schedule to a file before quitting? (Y/N): ").strip().upper()
                if save_choice == "Y":
                    filename = get_custom_filename_input()
                    print(save_schedule_to_file(formatted_list, filename))

            print("Exiting program... Goodbye!")
            break

        else:
            print("Please select valid option")

if __name__ == "__main__":
    mainMenu()
