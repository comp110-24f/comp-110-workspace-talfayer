"""CQ00"""

__author__ = "730646268"


def mimic(message: str) -> str:
    """Function that will return input as output"""
    return message


def main() -> None:
    """Main function pulls together functions"""
    print(mimic(message=input("What is your message")))


if __name__ == "__main__":
    main()
