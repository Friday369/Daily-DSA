#Time Complexity: O(n), Space Complexity: O(n)
def pairInSortedRotated(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

arr = [11, 15, 6, 8, 9, 10]
target = 16
print(pairInSortedRotated(arr, target))