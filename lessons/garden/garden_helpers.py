"""Some functions for my garden plan!"""

__author__ = "730676554"

by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
# want to get {"flower": ["marigold", "zinnia", "daisy"], "vegetable": ["carrots"]}


def add_by_kind(by_kind: dict[str, list[str]], type: str, name: str) -> None:
    """Adds a plant to a garden dictionary."""
    if type in by_kind:  # if the kind is already in the dictionary ("flower" was in by_kind)
        by_kind[type].append(name)
    else:  # if the kind is not the dictionary (e.g. "fruit" is not in by_kind)
        by_kind[type] = []
        by_kind[type].append(name)


by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"], "July": ["apples"]}


def add_by_date(by_date: dict[str, list[str]], month: str, name: str) -> None:
    """Adds a plant to a dictionary sorted by the date."""
    if month in by_date:
        by_date[month].append(name)
    else:
        by_date[month] = []
        by_date[month].append(name)


def lookup_by_kind_and_date(by_kind: dict[str, list[str]], by_date: dict[str, list[str]], type: str, month: str) -> str:
    """Searches thru both dictionaries and returns what kind of plants to plant at a certain date."""
    assert type in by_kind
    assert month in by_date
    # list all plants by kind
    kind_list: list[str] = by_kind[type] 
    # get a list of all plants planted in a specific month
    month_list: list[str] = by_date[month]
    # go through both lists and find elements that appear in both.
    combined_list: list[str] = []
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant:  # plant is in both kind_list and month_list
                combined_list.append(plant)

    if len(combined_list) > 0:
        return f'{type} to plant in {month}: {combined_list}'
    else:
        return f'No {type} to plant in {month}'