# NESTED LOOP EXAMPLES
# A loop inside another loop

print("Example 1: Times table grid")

for row in range(1, 4):
    for column in range(1, 4):
        print(row * column, end=" ")
    print()


print("\nExample 2: Simple pattern")

for row in range(1, 6):
    for column in range(row):
        print("#", end="")
    print()
