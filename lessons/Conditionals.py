"""Practicing my conditionals."""


def less_than_10(num: int) -> None:
    """Tell us if num<10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:  # check if this is true
        print("Small number!")  # "then" block
    else:
        print("Big number!")
    print("This is the end of the function!")
    # comes after the conditional so gets printed either way


less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """Rturn a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp 110!"
    else:
        return "Keep sleeping. You deserve it. :)"


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"
