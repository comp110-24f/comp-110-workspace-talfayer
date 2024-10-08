"""EX04 - list utility functions"""

__author__ = "730646268"


def all(input_list: list[int], num: int) -> bool:
    if len(input_list) == 0:
        return False
    for elem in input_list:
        if elem != num:
            return False
    return True


def max(input_list: list[int]) -> int:
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty list")  # empty list
    largest = input_list[0]  # assume first element is the largest in order to start it
    for elem in input_list:
        if (
            elem > largest
        ):  # compare each element (if [0]>[1], [0] stays largest and gets compared to [2], etc.)
            largest = elem  # largest gets reassigned the element
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    for index in range(0, len(list1)):
        if list1[index] != list2[index]:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    for elem in list2:
        list1.append(elem)  # add each element from list2 to list1
