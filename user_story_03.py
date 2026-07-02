# Checks if the course exists in list of avaliable courses
def is_valid_course(course_number, available_courses):
    return course_number in available_courses

# Checks if the student already selected this course
def is_duplicate_course(course_number, selected_course):
    return course_number in selected_course

# Adds course if it exists and has not already been selected
def add_course(course_number, available_courses, selected_courses):
   
    # Checks if course exists
    if not is_valid_course(course_number, available_courses):
        return "Error: Course does not exist."
    
    # Checks if course already selected
    if is_duplicate_course(course_number, selected_courses):
        return "Error: Course already selected."
    
    # Adds new course to list
    selected_courses.append(course_number)

    # Returns updated schedule
    return selected_courses
