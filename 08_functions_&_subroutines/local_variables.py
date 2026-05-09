# LOCAL VARIABLES
# A local variable only exists inside the function where it is created.

def calculate_bonus():
    bonus = 5
    print("Bonus inside function:", bonus)


calculate_bonus()

# This would cause an error because bonus only exists inside the function:
# print(bonus)
