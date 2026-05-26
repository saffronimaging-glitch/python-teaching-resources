import random
import time


# -----------------------------
# Bubble Sort
# -----------------------------
def bubble_sort(arr):
    arr = arr.copy()

    for i in range(len(arr)):

        for j in range(0, len(arr) - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# -----------------------------
# Merge Sort
# -----------------------------
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            result.append(left[i])
            i += 1

        else:

            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# -----------------------------
# Benchmarking Function
# -----------------------------
def benchmark(sort_function, data):

    start_time = time.perf_counter()

    sort_function(data)

    end_time = time.perf_counter()

    return end_time - start_time


# -----------------------------
# Main Benchmark Test
# -----------------------------
LIST_SIZE = 1000
TESTS = 10

bubble_total = 0
merge_total = 0

for test in range(TESTS):

    random_list = random.sample(range(1, 10000), LIST_SIZE)

    bubble_time = benchmark(bubble_sort, random_list)
    merge_time = benchmark(merge_sort, random_list)

    bubble_total += bubble_time
    merge_total += merge_time

    print(f"Test {test + 1}")
    print(f"Bubble Sort: {bubble_time:.6f} seconds")
    print(f"Merge Sort : {merge_time:.6f} seconds")
    print()


# -----------------------------
# Average Results
# -----------------------------
print("AVERAGE RESULTS")
print("--------------------------")

print(f"Average Bubble Sort: {bubble_total / TESTS:.6f} seconds")
print(f"Average Merge Sort : {merge_total / TESTS:.6f} seconds")
