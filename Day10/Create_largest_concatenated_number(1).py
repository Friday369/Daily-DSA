
# BRUTE FORCE
# Time: O(n! * n)  Space: O(n)

from itertools import permutations

def largestNumber_brute():
    arr = [3, 30, 34, 5, 9]
    max_num = ""

    for perm in permutations(arr):
        candidate = "".join(map(str, perm))
        if candidate > max_num:
            max_num = candidate

    print(f"Brute Force Result: {max_num}")

largestNumber_brute()