# Checks if the course exists in list of available courses
def is_valid_course(course_number, available_courses):
    return course_number in available_courses

# Checks if the student already selected this course
def is_duplicate_course(course_number, selected_courses):
    return course_number in selected_courses

# Adds course if it exists and has not already been selected
def add_course(course_number, available_courses, selected_courses):
    # Checks if course exists
    if not is_valid_course(course_number, available_courses):
        print("Error: Course does not exist.")
        return False
    
    # Checks if course already selected
    if is_duplicate_course(course_number, selected_courses):
        print("Error: Course already selected.")
        return False
    
    # Adds new course to list
    selected_courses.append(course_number)
    return True

# Allows student to enter courses
def enter_courses(available_courses):
    selected_courses = []
    while True:
        course_number = input("Enter a course number (or DONE to finish): ").upper()
            
        # Stops loop
        if course_number == "DONE":
            break

        success = add_course(course_number, available_courses, selected_courses)

        # Displays the list if course was added
        if success:
            display_selected_courses(selected_courses)

    return selected_courses

# Displays the student's selected courses 
def display_selected_courses(selected_courses):
    print("\nCurrent Course List:")
    if len(selected_courses) == 0:
        print("No courses selected.")
    else:
        for course in selected_courses:
            print(course)