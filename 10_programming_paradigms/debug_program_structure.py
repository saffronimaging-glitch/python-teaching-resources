# DEBUG THE PROGRAM STRUCTURE


# Debug 1
# This function should print a welcome message.

def welcome_message
    print("Welcome!")


# Debug 2
# The main program should call the function.

def display_menu():
    print("1 - Play")
    print("2 - Quit")


choice = input("Choose option: ")

if choice == "1":
    start_game()


# Debug 3
# This structure chart logic is incorrect.
# The score function should return a value.

def add_score(score):
    score = score + 1


current_score = 0

current_score = add_score(current_score)

print(current_score)
