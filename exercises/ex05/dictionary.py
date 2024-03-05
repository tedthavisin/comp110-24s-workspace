"""Multiple Functions."""

__author__ = "730676554"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values."""
    inverted_dict: dict[str, str] = {}
    for key in x:
        if x[key] in inverted_dict:
            raise KeyError("Duplicate keys.")
        inverted_dict[x[key]] = key
    return inverted_dict


def favorite_color(x: dict[str, str]) -> str:
    """Returns which color appears the most."""
    color: dict[str, int] = {}
    for key in x:
        if x[key] in color:
            color[x[key]] += 1
        else:
            color[x[key]] = 1
    highest: int = 0
    frequent_color: dict[str, str] = {}
    for key in color:
        if color[key] > highest:
            highest = color[key]
            frequent_color = key
    return frequent_color


def count(x: list[str]) -> dict[str, int]:
    """Produces a dict from a list."""
    count: dict[str, int] = {}
    for value in x:
        if value in count:
            count[value] = count[value] + 1
        else:
            count[value] = 1
    return count


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Produces dictionary where each key is a letter."""
    abet: dict[str, list[str]] = {}
    for word in x:
        if word[0] in abet:
            abet[word[0]].append(word)
        else:
            abet[word[0]] = word
    return abet


def update_attendance(x: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates attendance."""
    if day in x:
        x[day].append(student)
    else:
        x[day] = [student]
    return x



