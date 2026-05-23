# Merge Sort Example

numbers = [45, 12, 5, 4, 15, 21, 13]

print("Original list:")
print(numbers)


def merge_sort(list_to_sort):

    # Base case
    if len(list_to_sort) <= 1:
        return list_to_sort

    # Find middle point
    middle = len(list_to_sort) // 2

    # Split list into halves
    left_half = list_to_sort[:middle]
    right_half = list_to_sort[middle:]

    print(f"\nSplitting: {list_to_sort}")
    print(f"Left:  {left_half}")
    print(f"Right: {right_half}")

    # Recursively sort halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):

    merged = []

    left_index = 0
    right_index = 0

    print(f"\nMerging: {left} and {right}")

    # Compare values from both halves
    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:

            merged.append(left[left_index])
            left_index += 1

        else:

            merged.append(right[right_index])
            right_index += 1

    # Add remaining values
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    print(f"Merged result: {merged}")

    return merged


# Run merge sort
sorted_numbers = merge_sort(numbers)

print("\nSorted list:")
print(sorted_numbers)
