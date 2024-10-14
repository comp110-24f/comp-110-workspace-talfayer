from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(fruits) == "apples"


def test_remove_first_ret_value() -> None:  # testing the return value
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert (
        remove_first(fruits) == None
    )  # has to equal none because the function has a RV of none


def test_remove_first_behavior() -> None:  # testing the behavior
    fruits: list[str] = ["apples", "oranges", "bananas"]
    remove_first(fruits)
    assert fruits == [
        "oranges",
        "bananas",
    ]  # equals this bc the function is meant to remove the first value but has return none, so this is testing without the return
