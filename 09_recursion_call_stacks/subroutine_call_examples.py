# SUBROUTINE CALLS EXAMPLE
# This shows functions calling other functions.
# This is NOT recursion because no function calls itself.

def welcome_message():
    print("Welcome to the quiz game!")


def ask_name():
    name = input("What is your name? ")
    return name


def greet_player(name):
    print("Hello", name)
    print("Good luck!")


welcome_message()
player_name = ask_name()
greet_player(player_name)
