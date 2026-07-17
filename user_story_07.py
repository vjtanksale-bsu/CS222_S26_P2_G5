import os

def save_schedule_to_file(schedule, filename):
    """
    Save finalized student schedule to a text file, handle duplicate file overwrite prompt
    :param schedule: list of dict, each dict stores full course info
    :param filename: user custom output file name
    :return: status message string
    """
    if os.path.exists(filename):
        user_choice = input(f"File {filename} already exists. Overwrite? (Y/N): ").strip().upper()
        if user_choice != "Y":
            return "Save cancelled: User chose not to overwrite file, please input a new filename."
    
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("===== Student Final Schedule =====\n\n")
            for course in schedule:
                f.write(f"Course Number: {course['course_num']}\n")
                f.write(f"Section Number: {course['section']}\n")
                f.write(f"Meeting Days: {course['meeting_days']}\n")
                f.write(f"Start Time: {course['start_time']}\n")
                f.write(f"End Time: {course['end_time']}\n")
                f.write("-" * 40 + "\n")
        return f"Success! Schedule saved to file: {filename}"
    except Exception as e:
        return f"Save failed, error: {str(e)}"


def show_save_schedule_menu_option(valid_schedule_exists):
    """
    Only show save option in main menu when valid schedule is generated
    :param valid_schedule_exists: boolean, True if schedule can be saved
    """
    if valid_schedule_exists:
        print("\nMenu Option 7: Save Final Schedule to Text File")


def get_custom_filename_input():
    """Prompt user to enter custom output file name"""
    filename = input("Please enter a name for your schedule file (end with .txt): ").strip()
    if not filename.endswith(".txt"):
        filename = filename + ".txt"
    return filename

def run_save_schedule_workflow(current_schedule):
  
    if len(current_schedule) == 0:
        return "Cannot save: No valid schedule found, generate a schedule first."
    
    target_file = get_custom_filename_input()
    
    result_msg = save_schedule_to_file(current_schedule, target_file)
    print(result_msg)
    return result_msg
