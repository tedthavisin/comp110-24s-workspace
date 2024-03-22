"""Unit testing functions from dictionary.py file."""

__author__ = "740676554"

from exercises.ex05.dictionary import invert, count, favorite_color, alphabetizer, update_attendance


def test_invert_use_case_one() -> None:
    """Tests the invert function using a dictionary with letters, a-f."""
    input_dict: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    return_dict: dict[str, str] = invert(input_dict)
    assert return_dict == {"b": "a", "d": "c", "f": "e"}


def test_invert_use_case_two() -> None:
    """Tests the invert function using a dictionary with words."""
    input_dict: dict[str, str] = {"armor": "pool", "meow": "monkey", "egg": "fly"}  
    return_dict: dict[str, str] = invert(input_dict)
    assert return_dict == {"pool": "armor", "monkey": "meow", "fly": "egg"}


def test_invert_edge_case() -> None:
    """Tests the invert function using a blank key."""
    input_dict: dict[str, str] = {"": "b", "c": "d", "e": "f"}
    return_dict: dict[str, str] = invert(input_dict)
    assert return_dict == {"b": "", "d": "c", "f": "e"}


def test_count_use_case_one() -> None:
    """Tests the count function with a list with letters."""
    input_list: list[str] = ("a", "a", "b", "b", "b", "c", "d")
    return_dict: dict[str, int] = count(input_list)
    assert return_dict == {"a": 2, "b": 3, "c": 1, "d": 1}


def test_count_use_case_two() -> None:
    """Tests the count function with a list of names."""
    input_list: list[str] = ("Albert", "Daniel", "Albert", "Bethany", "Bernie", "Cathy", "Daniel")
    return_dict: dict[str, int] = count(input_list)
    assert return_dict == {"Albert": 2, "Daniel": 2, "Bethany": 1, "Bernie": 1, "Cathy": 1}


def test_count_edge_case() -> None:
    """Tests the count function using an empty list."""
    input_list: list[str] = ()
    return_dict: dict[str, int] = count(input_list)
    assert return_dict == {}


def test_favorite_color_use_case_one() -> None:
    """Tests the favorite_color function using a dictionary with names and colors."""
    input_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Ted": "green", "Kris": "blue"}
    return_value: str = favorite_color(input_dict)
    assert return_value == "blue"


def test_favorite_color_use_case_two() -> None:
    """Tests the favorite_color function using a dictionary with different names and colors."""
    input_dict: dict[str, str] = {"Fabian": "orange", "Matt": "pink", "Zack": "purple", "Tori": "pink"}
    return_value: str = favorite_color(input_dict)
    assert return_value == "pink"


def test_favorite_color_edge_case() -> None:
    """Tests the favorite_color function using a dictionary when there are the same amount of each color."""
    input_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Ted": "green", "Kris": "pink"}
    return_value: str = favorite_color(input_dict)
    # Keeps the first color unless another color is counted more.
    assert return_value == "yellow"


def test_alphabetizer_use_case_one() -> None:
    """Tests the alphabetizer function with objects."""
    input_list: list[str] = ("ball", "phone", "chapstick", "can", "apple")
    return_value: dict[str, list[str]] = alphabetizer(input_list)
    assert return_value == {"b": ["ball"], "p": ["phone"], "c": ["chapstick", "can"], "a": ["apple"]}


def test_alphabetizer_use_case_two() -> None: 
    """Tests the alphabetizer function with names."""    
    input_list: list[str] = ("Barry", "Phineas", "Carter", "Charles", "Arnold")
    return_value: dict[str, list[str]] = alphabetizer(input_list)
    assert return_value == {"b": ["Barry"], "p": ["Phineas"], "c": ["Carter", "Charles"], "a": ["Arnold"]}


def test_alphabetizer_edge_case() -> None:
    """Tests the alphabetizer function using list with only letters."""
    input_list: list[str] = ("b", "c", "d", "c")
    return_value: dict[str, list[str]] = alphabetizer(input_list)
    assert return_value == {"b": ["b"], "c": ["c", "c"], "d": ["d"]}


def test_update_attendance_use_case_one() -> None:
    """Tests the update_attendance function using "Tori" as the name and Tuesday as a date."""
    input_dict: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    input_day: str = "Tuesday"
    input_student: str = "Tori"
    update_attendance(input_dict, input_day, input_student)
    assert input_dict == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Tori"]}


def test_update_attendance_use_case_two() -> None:
    """Tests the update_attendance function using "Ted" as the name and Thursday as a new date."""
    input_dict: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    input_day: str = "Thursday"
    input_student: str = "Ted"
    update_attendance(input_dict, input_day, input_student)
    assert input_dict == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Thursday": ["Ted"]}


def test_update_attendance_edge_case() -> None:
    """Tests the update_attendance function using a blank name and Tuesday as the day."""
    input_dict: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    input_day: str = "Tuesday"
    input_student: str = ""
    update_attendance(input_dict, input_day, input_student)
    assert input_dict == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", ""]}
