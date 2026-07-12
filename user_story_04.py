# Checks if the generated schedule is empty
def is_empty_schedule(schedule):
    return len(schedule) == 0

# Creates formatted schedule for the student to view
def display_schedule(schedule):

    # Checks if the schedule is empty
    if is_empty_schedule(schedule):
        return "No schedule available"
    
    # Creates the schedule heading
    output = "Generated Schedule:\n"
    
    # Adds each course's information to the schedule
    for course in schedule:
        output += "\nCourse Number: " + course["course"]
        output += "\nSection Number: " + course["section"]
        output += "\nMeeting Days: " + course["days"]
        output += "\nMeeting Time: " + course["start"] + "-" + course["end"] + "\n"
    
    # Returns the completed schedule
    return output

