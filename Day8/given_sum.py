#Time Complexity: O(n), Space Complexity: O(1)
def pairInSortedRotated(arr, target):
    n = len(arr)

    # Step 1: find the pivot (index of the largest element)
    i = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            break
    if arr[i] <= arr[i + 1]:
        i += 1   # array was fully sorted, no rotation

    # Step 2: set up pointers
    left = (i + 1) % n   # index of smallest element
    right = i            # index of largest element

    # Step 3: two-pointer scan across the circular array
    while left != right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n

    return False

arr = [11, 15, 6, 8, 9, 10]
target = 16
print(pairInSortedRotated(arr, target))