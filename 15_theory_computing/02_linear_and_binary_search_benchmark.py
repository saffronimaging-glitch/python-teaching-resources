import random
import time

# ---------- Linear Search ----------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# ---------- Binary Search ----------
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# ---------- Benchmark Setup ----------
# Change these inputs to determine the point things get "out of hand"
LIST_SIZE = 10000
TESTS = 1000

# Create sorted list
numbers = list(range(LIST_SIZE))

# Random targets to search for
targets = [random.randint(0, LIST_SIZE - 1) for _ in range(TESTS)]


# ---------- Benchmark Linear Search ----------
start = time.perf_counter()

for target in targets:
    linear_search(numbers, target)

end = time.perf_counter()

linear_time = end - start


# ---------- Benchmark Binary Search ----------
start = time.perf_counter()

for target in targets:
    binary_search(numbers, target)

end = time.perf_counter()

binary_time = end - start


# ---------- Results ----------
print(f"Linear Search Time : {linear_time:.6f} seconds")
print(f"Binary Search Time : {binary_time:.6f} seconds")
