# DEBUG THE RECURSION


# Debug 1
# This countdown should stop at 1.

def countdown(number):
    print(number)
    countdown(number - 1)


countdown(5)


# Debug 2
# This factorial function should return 24 when given 4.

def factorial(number):
    if number == 1:
        return 1
    else:
        number * factorial(number - 1)


print(factorial(4))


# Debug 3
# This function should count down towards the base case.

def recursive_count(number):
    if number == 1:
        print("Done")
    else:
        recursive_count(number + 1)


recursive_count(5)


# Debug 4
# This function should call itself, but the function name is wrong.

def say_hello(times):
    if times == 0:
        print("Finished")
    else:
        print("Hello")
        repeat_hello(times - 1)


say_hello(3)
