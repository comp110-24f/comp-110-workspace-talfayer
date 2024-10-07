"""for loops"""

xs: list[str] = ["w", "x", "y", "z"]

index: int = 0

while index < len(xs):
    print(xs[index])
    index += 1

for elem in xs:
    print(elem)

my_list: list[str] = ["hello", "world"]
new_list: list[str] = []
for elem in my_list:
    new_list.append(elem)
print(new_list)

pets: list[str] = ["Louie", "Bo", "Bear"]
for name in pets:
    print(f"Good boy, {name}!")  # "Good boy," + animal + "!"

names: list[str] = ["Alyssa", "Janet", "Vrinda"]  # using range() in a for...in... loop
# print each index: name
index: int = 0
for index in range(0, len(names)):
    print(f"{index}: {names[index]}")
