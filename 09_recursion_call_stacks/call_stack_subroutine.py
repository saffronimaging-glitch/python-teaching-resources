# CALL STACK WITH SUBROUTINES
# Each function call is added to the call stack.
# When a function finishes, it is removed from the stack.

def main():
    print("main() starts")
    play_game()
    print("main() ends")


def play_game():
    print("  play_game() starts")
    ask_question()
    print("  play_game() ends")


def ask_question():
    print("    ask_question() starts")
    print("    What is 2 + 2?")
    print("    ask_question() ends")


main()
