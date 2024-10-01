"""CQ03"""

__author__ = "730646268"


def num_instances(phrase: str, search_char: str) -> None:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1  # index has to be on same line as if cuz want it to happen regardless of if statement
    print(count)


num_instances(phrase="When", search_char="e")
