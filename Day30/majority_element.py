# OPTIMAL — Moore's Voting Algorithm
# Time: O(n)  Space: O(1)
def majorityElement_optimal():
    arr = [1, 1, 2, 1, 3, 5, 1]
    n = len(arr)
    candidate = -1
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    count = 0
    for num in arr:
        if num == candidate:
            count += 1
    if count > n // 2:
        print(f"Optimal Result: {candidate}")
    else:
        print("Optimal Result: -1")
majorityElement_optimal()