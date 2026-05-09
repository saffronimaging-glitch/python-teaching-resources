# STRETCH CHALLENGE - RECURSIVE SUM
# Add all numbers from n down to 1.
# Example:
# recursive_sum(5) = 5 + 4 + 3 + 2 + 1 = 15

def recursive_sum(number):
    if number == 1:
        return 1
    else:
        return number + recursive_sum(number - 1)


print(recursive_sum(5))


# Extra stretch:
# Can you write an iterative version using a for loop?
# Can you print each call as it happens?
