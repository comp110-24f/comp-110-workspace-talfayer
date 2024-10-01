"""EX02 - Chardle - small step towards Wordle"""

__author__ = "730646268"


def input_word() -> str:
    word: str = str(input("Enter a 5-character word: "))
    if len(word) == 5:
        return word
    elif len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # use the exit so the program doesn't continue since the word wasn't good
    return word


def input_letter() -> str:
    letter: str = str(input("Enter a single character: "))
    if len(letter) == 1:
        return letter
    elif len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    count: int = 0
    print("Searching for", letter, "in", word)
    if (
        word[0] == letter
    ):  # remember the : after if/elif statements # asks if the first letter of the word matches the letter
        print(letter, "found at index 0")
        count = count + 1
    if (
        word[1] == letter
    ):  # this repeating lines tells you if each letter (different index) matches the letter
        print(letter, "found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter, "found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter, "found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter, "found at index 4")
        count = count + 1
    if count == 0:
        print(
            "No instances of", letter, "found in", word
        )  # if none of the input letter are found in the word
    if count == 1:
        print(count, "instance of", letter, "found in", word)
    if count >= 1:
        print(
            count, "instances of", letter, "found in", word
        )  # difference between the word instance when count=1 and instances when count >=1
    print(str(count), " instances of ", str(letter), "found in", str(word))


def main() -> None:  # combining all the functions under one main function
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
