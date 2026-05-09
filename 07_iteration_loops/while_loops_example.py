# WHILE LOOP EXAMPLES
# Indefinite iteration = repeat until a condition is met

print("Example 1: Countdown")

count = 5

while count > 0:
    print(count)
    count = count - 1

print("Blast off!")


print("\nExample 2: Keep asking until correct")

answer = ""

while answer.lower() != "paris":
    answer = input("What is the capital of France? ")

print("Correct!")
