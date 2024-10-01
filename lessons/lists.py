"""introduction to lists practice"""

my_numbers: list[float] = []
my_numbers.append(1.5)

game_points: list[int] = [102, 86, 94]
game_points[1] = 72
game_points.pop(1)
print(game_points)
