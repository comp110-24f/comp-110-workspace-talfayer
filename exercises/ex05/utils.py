"""EX05 list utility function"""

__author__ = "730646268"


def only_evens(nums: list[int]) -> list[int]:
    list_evens: list[int] = []
    for elem in nums:
        if elem % 2 == 0:
            list_evens.append(elem)
    return list_evens


def sub(nums: list[int], start: int, end: int) -> list[int]:
    if len(nums) == 0 or start >= len(nums) or end <= 0:
        return []
    if start < 0:  # adjust the start and end values
        start = 0
    if end > len(nums):
        end = len(nums)
    list_mutated: list[int] = []  # build the result list
    for elem in range(start, end):  # end not inclusive
        list_mutated.append(nums[elem])  # adding the numbers to the empty set
    return list_mutated


def add_at_index(list: list[int], added: int, index: int) -> None:
    """Adds number at specific index"""
    if index < 0 or index > len(list):
        raise IndexError("Index is out of bounds for the input list")
    list.append(0)  # have to add an empty spot at the end to be able to shift the list
    for i in range(
        len(list) - 1, index, -1
    ):  # elem is the different numbers in the list
        """shifts to the right"""
        list[i] = list[
            i - 1
        ]  # reassigning the 4th number (0) to be equal to the number before so could replace the number before without taking out a number
    list[index] = added
