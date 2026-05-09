# PROCEDURAL PROGRAMMING EXAMPLE
# The program follows a sequence of procedures/functions.

def welcome():
    print("Welcome to the game!")


def show_menu():
    print("1 - Play")
    print("2 - Quit")


def play_game():
    print("Game starting...")


# Main sequence

welcome()

show_menu()

choice = input("Choose an option: ")

if choice == "1":
    play_game()

else:
    print("Program ended.")
