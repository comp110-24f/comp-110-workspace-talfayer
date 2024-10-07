""""Mutating functions."""

__author__ = "730646268"


def manual_append(list: list[int], num: int) -> None:
    list.append(num)


def double(list: list[int]) -> None:
    idx: int = 0
    while idx < len(list):
        list[idx] = list[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


double(list_2)

print(list_1)
print(list_2)
