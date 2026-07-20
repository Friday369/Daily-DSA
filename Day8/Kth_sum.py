#Time Complexity: O(n) on average, O(n^2) in worst case, Space Complexity: O(1)
import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quickSelect(arr, low, high, k_index):
    if low == high:
        return arr[low]

    # randomize pivot to avoid worst-case O(N^2) on sorted/adversarial input
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

    pivot_index = partition(arr, low, high)

    if pivot_index == k_index:
        return arr[pivot_index]
    elif pivot_index < k_index:
        return quickSelect(arr, pivot_index + 1, high, k_index)
    else:
        return quickSelect(arr, low, pivot_index - 1, k_index)

def kthSmallest_optimal(arr, k):
    n = len(arr)
    return quickSelect(arr, 0, n - 1, k - 1)

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kthSmallest_optimal(arr, k))