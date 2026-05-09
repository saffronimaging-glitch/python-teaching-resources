# FIBONACCI RECURSION
# Fibonacci sequence:
# 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)


for i in range(8):
    print("Position", i, "=", fibonacci(i))
