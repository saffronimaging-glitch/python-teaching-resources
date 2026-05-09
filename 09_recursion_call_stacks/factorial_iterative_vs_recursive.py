# FACTORIAL - ITERATION VS RECURSION
# 4! means 4 x 3 x 2 x 1

print("ITERATIVE VERSION")


def factorial_iterative(number):
    total = 1

    for i in range(number, 0, -1):
        total = total * i

    return total


print("4! =", factorial_iterative(4))


print("\nRECURSIVE VERSION")


def factorial_recursive(number):
    if number == 1:
        return 1
    else:
        return number * factorial_recursive(number - 1)


print("4! =", factorial_recursive(4))
