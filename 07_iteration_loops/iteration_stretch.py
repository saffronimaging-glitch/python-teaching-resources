# STRETCH CHALLENGE - PATTERN GENERATOR

# Task:
# Ask the user for a symbol and a height.
# Then print a triangle pattern using that symbol.

symbol = input("Choose a symbol: ")
height = int(input("Choose a height: "))

for row in range(1, height + 1):
    for column in range(row):
        print(symbol, end="")
    print()


# Extra stretch:
# Can you make the pattern count backwards?
# Example:
# #####
# ####
# ###
# ##
# #
