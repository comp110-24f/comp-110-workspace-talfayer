"""practicing function writing"""


# number 6
def size_strings(strings: list[str]) -> list[int]:
    result: list[int] = []
    for x in range(0, len(strings)):
        result.append(len(strings[x]))
    return result


# number 7
def sum(strings: list[str]) -> int:
    result: int = 0
    for elem in strings:
        result += len(elem)
    return result


# number 8
def exclamation(strings: list[str]) -> None:
    for elem in strings:
        elem = f"{elem}!"


# number 9
def list(word: str) -> list[str]:
    idx: int = 0
    list1: list[str] = []
    while idx < len(word):
        list1 += word[idx]
        idx += 1
    return list1


# or
def characters(word: str) -> list[str]:
    result: list[str] = []
    for elem in word:
        result.append(elem)
    return result


# numb er 10
# number 11
def list_floats(floats: list[float], index: int, insert: float) -> list[float]:
   result: list[float] = []
   for x in range(0, len(floats)):
       if x == index:
           result.append(insert)
        result.append(floats[x])
    if index >= len(floats):
       result.append(insert)
    return result

#12
def only_even(nums: list[int]) -> list[int]:
    evens: list[int] = []
    for elem in nums:
        if elem%2 == 0:
            evens.append(elem)
    return evens

#13
def only_a(words: list[str]) -> list[str]:
    result: list[str] = []
    for word in words:
        for letter in word:
            if letter == "a":
                result.append(word)
    return result
#or
def only_a(words: list[str]) -> list[str]:
    result: list[str] = []
    for word in words:
        if 'a' in word:
            result.append(word)
    return result
#14
def largest(nums: list[int]) -> int:
    large: int = 0
    for idx in range(0, len(nums)):
        if nums[idx] > nums[idx+1]:
            large = nums[idx]
    return large
#15
#22
def only_even(dict: dict[str, int]) -> list[int]:
    result: list[int] = []
    for key in dict:
        if dict[key] % 2 == 0:
            result.append(key)
    return result
#23
def largest_key(dict[str, int]) -> str:
    largest: int = 0 
    largestkey: str = ""
    for key in dict:
        if dict[key] > largest:
            largest = dict[key]
            largestkey = key
    return largestkey
#24
def merge_dict(dict1: dict[str, float], dict2: dict[str, float]) -> dict[str, float]:
    result: dict[str, float]: {}
    for key in dict1:
        result[key] = dict1[key]
    for key in dict2:
        if key in result:
            result[key] += dict2[key]
        else:
            result[key] = dict2[key]
    return result