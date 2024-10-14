"""practicing functions"""


def get_first(a: list[str]) -> str:
    return a[0]


def remove_first(b: list[str]) -> None:
    b.pop(0)


def get_and_remove_first(c: list[str]) -> str:
    d = c[0]
    c.pop(0)
    return d


print(get_and_remove_first(["hi", "hello", "how are you"]))
