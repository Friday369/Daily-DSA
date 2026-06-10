 #OPTIMAL — Min Heap
# Time: O(n log k)  Space: O(k)

import heapq
def findKthLargest():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  

    print(f"Optimal Result: {min_heap[0]}")

findKthLargest()