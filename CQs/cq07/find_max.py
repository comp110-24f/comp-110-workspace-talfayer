"""CQ07 find max"""

__author__ = "730646268"


def find_and_remove_max(list: list[int]) -> int:
    """Find the largest number in the list and delete thte largest number"""
    max_num: int = 0
    i: int = 0  # index
    if list == []:
        return -1
    for elem in list:
        if (
            elem > max_num
        ):  # starts at 0 so first number is automatically largest then becomes max_num
            max_num = elem
    while i < len(list):  # loops through every index
        if list[i] == max_num:  # if the index is the max number then use pop
            list.pop(i)
        else:
            i += 1  # increase index
    return max_num
