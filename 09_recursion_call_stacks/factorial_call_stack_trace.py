# FACTORIAL CALL STACK TRACE
# This version prints what is happening as the recursive calls build up and return.

def factorial(number):
    print("Calling factorial(" + str(number) + ")")

    if number == 1:
        print("Base case reached: factorial(1) returns 1")
        return 1
    else:
        print("Waiting for factorial(" + str(number - 1) + ")")
        result = number * factorial(number - 1)
        print("Returning", result, "from factorial(" + str(number) + ")")
        return result


answer = factorial(4)

print("Final answer:", answer)
