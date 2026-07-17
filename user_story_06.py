# Checks if the course is in the student's selected course list
def course_is_selected(course_number, selected_courses):
    return course_number in selected_courses


# Removes a course from the student's selected course list
def remove_course(course_number, selected_courses):

    # Checks if the course is currently selected
    if not course_is_selected(course_number, selected_courses):
        return "Error: Course is not in the current list."

    # Removes the course from the list
    selected_courses.remove(course_number)

    # Returns the updated course list
    return selected_courses


# Displays the student's updated course list
def display_updated_courses(selected_courses):

    output = "Current Course List:\n"

    # Checks if the course list is empty
    if len(selected_courses) == 0:
        return output + "No courses selected."

    course_number = 1

    # Adds each remaining course to the numbered list
    for course in selected_courses:
        output += str(course_number) + ". " + course + "\n"
        course_number += 1

    return output


# Allows the student to remove a course
def remove_selected_course(selected_courses):

    course_number = input("Enter the course number to remove: ").upper()

    result = remove_course(course_number, selected_courses)

    # Displays an error if the course is not found
    if isinstance(result, str):
        print(result)
        return False

    # Displays the updated course list
    print(display_updated_courses(selected_courses))
    return True