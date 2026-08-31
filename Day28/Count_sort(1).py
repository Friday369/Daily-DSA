#time Complexity: O(n log n)
#Space Complexity: O(n+k)
def countingSort_brute(arr):
    return sorted(arr)

arr = [4, 3, 12, 1, 5, 5, 3, 9]
print(countingSort_brute(arr))