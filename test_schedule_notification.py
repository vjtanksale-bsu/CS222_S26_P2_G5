import io
import sys
from schedule_generator import ScheduleGenerator

def capture_stdout():
    capture = io.StringIO()
    sys.stdout = capture
    return capture

def reset_stdout():
    sys.stdout = sys.__stdout__

def test_detect_valid_invalid_schedule():
    conflict = [
        {"num":"ENG104", "days":["M"], "start":9, "end":11},
        {"num":"COMM210", "days":["M"], "start":10, "end":12}
    ]
    gen = ScheduleGenerator(conflict)
    assert gen.has_valid_schedule() is False

    safe = [
        {"num":"ENG104", "days":["M"], "start":9, "end":11},
        {"num":"COMM210", "days":["T"], "start":10, "end":12}
    ]
    gen2 = ScheduleGenerator(safe)
    assert gen2.has_valid_schedule() is True

def test_check_all_selected_courses():
    three_courses = [
        {"num":"CS121", "days":["W"], "start":13, "end":15},
        {"num":"MATH101", "days":["W"], "start":14, "end":16},
        {"num":"STAT200", "days":["W"], "start":13, "end":17}
    ]
    gen = ScheduleGenerator(three_courses)
    gen.generate_schedule()
    assert gen.checked_course_count == 3

def test_show_notification_when_no_schedule():
    conflict = [
        {"num":"ENG104", "days":["M"], "start":9, "end":11},
        {"num":"COMM210", "days":["M"], "start":10, "end":12}
    ]
    gen = ScheduleGenerator(conflict)
    cap = capture_stdout()
    gen.generate_schedule()
    out = cap.getvalue()
    reset_stdout()
    assert "No valid schedule could be found. Please select different courses." in out

def test_no_schedule_display_when_invalid():
    conflict = [
        {"num":"ENG104", "days":["M"], "start":9, "end":11},
        {"num":"COMM210", "days":["M"], "start":10, "end":12}
    ]
    gen = ScheduleGenerator(conflict)
    cap = capture_stdout()
    gen.generate_schedule()
    out = cap.getvalue()
    reset_stdout()
    assert "Course Number" not in out
    assert "Meeting Time" not in out
