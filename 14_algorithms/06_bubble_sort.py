# Bubble Sort Example

numbers = [45, 12, 5, 4, 15, 21, 13]

print("Original list:")
print(numbers)


# Bubble Sort Algorithm

for i in range(len(numbers)):

    swapped = False

    for j in range(0, len(numbers) - i - 1):

        print(f"Comparing {numbers[j]} and {numbers[j + 1]}")

        # Swap if values are in the wrong order
        if numbers[j] > numbers[j + 1]:

            print(f"Swapping {numbers[j]} and {numbers[j + 1]}")

            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

            swapped = True

            print(numbers)

    # Stop early if already sorted
    if swapped == False:
        break


print("\nSorted list:")
print(numbers)
