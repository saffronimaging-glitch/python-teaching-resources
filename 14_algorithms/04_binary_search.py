# Binary Search Example
# The list MUST be sorted for binary search

numbers = [4, 5, 12, 13, 15, 21, 45]

target = 15

low = 0
high = len(numbers) - 1

found = False


while low <= high:

    middle = (low + high) // 2

    print(f"Checking middle index {middle}: {numbers[middle]}")

    # Target found
    if numbers[middle] == target:

        print(f"{target} found at index {middle}")
        found = True
        break

    # Search right half
    elif numbers[middle] < target:

        low = middle + 1

    # Search left half
    else:

        high = middle - 1


if found == False:
    print("Number not found")
