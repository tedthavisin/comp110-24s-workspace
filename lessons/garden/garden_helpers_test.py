"""Test my garden functions."""

__author__ = "730676554"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_new_kind() -> None:
    """New kind of plant."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    after: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"], "fruit": ["apples"]}
    type: str = "fruit"
    name: str = "apples"
    add_by_kind(by_kind, type, name)
    assert by_kind == after


def test_add_by_kind_empty_input() -> None:
    """Test if name & type variable is empty."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    type: str = ""
    name: str = ""
    add_by_kind(by_kind, type, name)
    assert by_kind == {'flower': ['marigold', 'zinnia'], 'vegetable': ['carrots'], '': ['']}


def test_add_by_date_new_date() -> None:
    """Tests if new month is added if not already on the dictionary."""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    month: str = "December"
    name: str = "nightshade"
    add_by_date(by_date, month, name)
    assert by_date == {'April': ['marigold'], 'June': ['carrots'], 'December': ['nightshade']}


def test_add_by_date_empty_date() -> None:
    """Tests when month input is empty."""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    month: str = ""
    name: str = "nightshade"
    add_by_date(by_date, month, name)
    assert by_date == {'April': ['marigold'], 'June': ['carrots'], '': ['nightshade']}


def test_lookup_by_kind_and_date_no_plant_during_month() -> None:
    """Tests when there is no plants to plant during the month inputted."""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    type: str = "flower"
    month: str = "June"
    assert "No flower to plant in June" == lookup_by_kind_and_date(by_kind, by_date, type, month)


def test_lookup_by_kind_and_date_capitalization() -> None:
    """Tests when by_date and month include different capitalization."""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"], "JULY": ["apples"]}
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"], "fruits": ["apples"]}
    type: str = "flower"
    month: str = "JULY"
    assert (lookup_by_kind_and_date(by_kind, by_date, type, month)) == "No flower to plant in JULY"