"""CQ04 coordinates"""

__author__ = "730646268"


def get_coords(xs: str, ys: str) -> None:
    indexx = 0
    indexy = 0
    while indexx < len(xs):
        while indexy < len(ys):
            print(xs[indexx], ys[indexy])
            indexy += 1
        indexy = 0
        indexx += 1
