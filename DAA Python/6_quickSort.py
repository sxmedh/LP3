import random

def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_index = deterministic_partition(arr, low, high)

        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)

        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Original array:", arr)

# Deterministic Quicksort
deterministic_quicksort(arr.copy(), 0, len(arr) - 1)
print("Sorted array (deterministic):", arr)

# Randomized Quicksort
randomized_quicksort(arr.copy(), 0, len(arr) - 1)
print("Sorted array (randomized):", arr)
