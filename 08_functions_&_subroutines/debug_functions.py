# DEBUG THE FUNCTIONS


# Debug 1
# This function should print a welcome message.

def welcome_message
    print("Welcome to the quiz!")


welcome_message()


# Debug 2
# This function should greet the player by name.

def greet_player():
    print("Hello", player_name)


greet_player("David")


# Debug 3
# This function should return the total.

def add_numbers(num1, num2):
    total = num1 + num2


answer = add_numbers(5, 7)

print(answer)


# Debug 4
# This quiz function should return 1 if the answer is correct.

def check_answer(user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
        return 1
    else:
        return 0


score = 0

score + check_answer("Paris", "Paris")

print("Score:", score)
