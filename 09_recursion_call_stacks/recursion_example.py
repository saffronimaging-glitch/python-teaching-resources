# BASIC RECURSION - COUNTDOWN
# Recursion is when a function calls itself.

def countdown(number):
    print(number)

    if number == 1:
        print("Blast off!")
    else:
        countdown(number - 1)


countdown(5)
