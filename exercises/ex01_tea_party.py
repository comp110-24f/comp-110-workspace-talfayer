"""Throwing a giant tea party"""

__author__: str = "730646268"


def main_planner(guests: int) -> None:
    """implementing a function to bring all of these functions together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=(treats(people=guests)))
        )
    )


# have to print as strings added together so use "" and +
# remember to close all parenthesis


def tea_bags(people: int) -> int:
    """defining tea_bags function
    people: the number of guests attending the tea party"""
    return people * 2


def treats(people: int) -> int:
    """defining the treats function to compute the number of treats
    based on the number of guests"""
    return int((tea_bags(people=people)) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """function to compute the cost of the tea bags and the treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
