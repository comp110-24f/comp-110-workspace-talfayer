"""CQ07 test max"""

__author__ = "730646268"

from find_max import find_and_remove_max


def test_return_find_and_remove_max() -> None:  # tests the return value
    """Tests to make sure the functions returns the right max"""
    assert find_and_remove_max([1, 2, 2, 1, 3, 3]) == 4


def test_mutate_find_and_remove_max() -> None:  # mutate tests the actual functioning
    """Tests to make sure function removes the max"""
    test_list: list[int] = [1, 2, 4, 2, 2, 4]
    find_and_remove_max(test_list)
    assert 4 not in test_list


def test_inbounds_find_and_remove_max() -> None:
    """Makes sure the function returns the right output if unconventional input"""
    list1: list[int] = []
    assert find_and_remove_max(list1) == -1
