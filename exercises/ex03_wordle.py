"""EX03: Wordle"""

__author__ = "730646268"


def input_guess(secret_word_len: int) -> str:
    word: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # input uses the f-string - make note of the format (need the braces bracket)
    while len(word) != secret_word_len:
        word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return word


def contains_char(input_word: str, character: str) -> bool:
    """This function is going to check if a specific character is found at any index in the input word"""
    assert len(character) == 1
    index: int = 0
    while index < len(
        input_word
    ):  # once index is not less than the len it will go to return false
        if input_word[index] == character:
            return True
        index += 1  # so continues in the while loop
    return False


def emojified(word_guess: str, secret_word: str) -> str:
    """This function will use emojis to visually describe the accuracy of a guess"""
    assert len(word_guess) == len(secret_word)  # ensures both strings are equal lengths
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    index: int = 0
    while index < len(word_guess):
        if (
            word_guess[index] == secret_word[index]
        ):  # first check if the [index] of both words are equal with an if statement
            result += GREEN_BOX
        elif contains_char(
            secret_word, word_guess[index]
        ):  # if first condition is false, check if the [index] is anywhere in the word using the contains_char function which tests if the characters are in the secret word
            result += YELLOW_BOX
        else:  # if both conditions are false than the letter isn't in the secret word so white box
            result += WHITE_BOX
        index += 1  # to check every index
    return result


def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # new variable to keep track of the turns
    while turn <= 6:  # can go up to 6 so =
        print(f"=== Turn {turn}/6 ===")
        word_guess: str = input_guess(
            len(secret_word)
        )  # using the input_guess functions to integrate the guessed word
        print(emojified(word_guess, secret_word))
        if word_guess == secret_word:
            print(f"You won in {turn}/6 turns!")
            return None
        turn += 1  # keep the loop going
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":  # used so can run program as a module
    main("hello")
