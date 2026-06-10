# BRUTE FORCE
# Time: O(n! * n)  Space: O(n!)

from itertools import permutations
def nextPermutation():
    nums = [1, 2, 3]
    all_perms = sorted(set(permutations(nums)))
    current = tuple(nums)
    for i in range(len(all_perms)):
        if all_perms[i] == current:
            if i == len(all_perms) - 1:
                result = list(all_perms[0])
            else:
                result = list(all_perms[i + 1])
            break
    print(f"Brute Force Result: {result}")

nextPermutation()