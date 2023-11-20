import random

# Deterministic QuickSort
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choosing middle element as pivot
        lesser = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return deterministic_quicksort(lesser) + equal + deterministic_quicksort(greater)

# Randomized QuickSort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)  # Choosing pivot randomly
        lesser = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return randomized_quicksort(lesser) + equal + randomized_quicksort(greater)

# Example usage:
arr = [7, 2, 1, 6, 8, 5]
print("Original Array:", arr)

sorted_deterministic = deterministic_quicksort(arr.copy())
print("Sorted Array using Deterministic QuickSort:", sorted_deterministic)

sorted_randomized = randomized_quicksort(arr.copy())
print("Sorted Array using Randomized QuickSort:", sorted_randomized)