"""CQ02"""

__author__ = "730646268"


def guess_a_number() -> None:
    """This function is a number guessing game"""
    secret: int = 7  # defining a local variable
    x: int = int(
        input("Guess a number:")  # asks the player to guess a number
    )  # defines x so that it is the number the user inputs
    print("Your guess was", x)
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is 7")
    elif x > secret:  # use another elif because else can't have conditional
        print("Your guess was too high! The secret number is 7")


if __name__ == "__main__":
    guess_a_number()
