"""Learning the for-in loop bruh!"""

names: list[str] = ["jonathan", "Jason", "jae", "jolly"]

# while loop
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1


# for in loop
for name in names:
    print(name)