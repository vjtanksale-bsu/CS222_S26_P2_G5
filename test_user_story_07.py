import os
from user_story_07 import save_schedule_to_file, run_save_schedule_workflow, show_save_schedule_menu_option

test_valid_schedule = [
    {
        "course_num": "CS222",
        "section": "01",
        "meeting_days": "Mon/Wed/Fri",
        "start_time": "09:00",
        "end_time": "10:15"
    },
    {
        "course_num": "ENG104",
        "section": "02",
        "meeting_days": "Tue/Thu",
        "start_time": "13:30",
        "end_time": "14:45"
    }
]
test_filename = "test_schedule_output.txt"

def test_save_option_only_appears_with_valid_schedule():
    assert show_save_schedule_menu_option(False) is None
    assert show_save_schedule_menu_option(True) is None

def test_file_writes_full_course_details():
    save_schedule_to_file(test_valid_schedule, test_filename)
    with open(test_filename, "r", encoding="utf-8") as f:
        file_content = f.read()
    assert "Course Number: CS222" in file_content
    assert "Section Number: 01" in file_content
    assert "Meeting Days: Mon/Wed/Fri" in file_content
    assert "Start Time: 09:00" in file_content
    assert "End Time: 10:15" in file_content
    os.remove(test_filename)

def test_empty_schedule_block_save():
    empty_schedule = []
    message = run_save_schedule_workflow(empty_schedule)
    assert "No valid schedule found" in message

def test_save_success_message_displayed(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "my_schedule")
    run_save_schedule_workflow(test_valid_schedule)
    captured_text = capsys.readouterr().out
    assert "Success! Schedule saved to file: my_schedule.txt" in captured_text
    os.remove("my_schedule.txt")

def test_duplicate_file_confirm_override(monkeypatch):
    open(test_filename, "w").close()
    monkeypatch.setattr("builtins.input", lambda _: "N")
    msg = save_schedule_to_file(test_valid_schedule, test_filename)
    assert "Save cancelled" in msg
    os.remove(test_filename)
