# CALL STACK WITH SUBROUTINES
# Each function call is added to the call stack.
# When a function finishes, it is removed from the stack.

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


# Example usage
print(factorial(5))
