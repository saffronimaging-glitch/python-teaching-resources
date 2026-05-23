# Linear Search Example
# Searching for the number 15

numbers = [45, 12, 5, 4, 15, 21, 13]

target = 15

found = False


for index in range(len(numbers)):

    print(f"Checking index {index}: {numbers[index]}")

    if numbers[index] == target:

        print(f"{target} found at index {index}")
        found = True
        break


if found == False:
    print("Number not found")
