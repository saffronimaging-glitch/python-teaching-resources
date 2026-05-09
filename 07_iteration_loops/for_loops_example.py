# FOR LOOP EXAMPLES
# Definite iteration = repeat a known number of times

print("Example 1: Count from 1 to 5")

for number in range(1, 6):
    print(number)


print("\nExample 2: Repeat a message 3 times")

for i in range(3):
    print("Keep practising Python!")


print("\nExample 3: Loop through quiz questions")

questions = [
    "What is 2 + 2?",
    "What is the capital of France?",
    "What keyword creates a function in Python?"
]

for question in questions:
    print(question)
