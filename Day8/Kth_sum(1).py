#Time Complexity: O(n log k), Space Complexity: O(k)
import heapq

def kthSmallest_heap(arr, k):
    heapq.heapify(arr)
    smallest = None
    for _ in range(k):
        smallest = heapq.heappop(arr)
    return smallest

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kthSmallest_heap(arr, k))