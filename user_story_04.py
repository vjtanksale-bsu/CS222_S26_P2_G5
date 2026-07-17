# Checks if the generated schedule is empty
def is_empty_schedule(schedule):
    return len(schedule) == 0

# Creates formatted schedule for the student to view
def display_schedule(schedule):

    # Checks if schedule is empty
    if is_empty_schedule(schedule):
        return "No schedule available"
    
    # Creates the schedule heading
    output = "Generated Schedule:\n"
    
    # Adds each course's information to the schedule
    for course in schedule:
        output += "\n------------------"
        output += "\nCourse Number: " + course["course"]
        output += "\nSection Number: " + course["section"]
        output += "\nMeeting Days: " + course["days"]
        output += "\nMeeting Time: " + course["start"] + " - " + course["end"] + "\n"
    
    # Returns the completed schedule
    return output

# Displays the main menu
def main_menu(schedule):
    print("1. View Generated Schedule")
    print("2. Exit")

    choice = input("Select an option: ")

    # Displays the generated schedule
    if choice == "1":
        print(display_schedule(schedule))
    # Exits 
    else:
        print("Exiting...")
