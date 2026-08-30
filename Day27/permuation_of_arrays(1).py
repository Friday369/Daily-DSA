# BRUTE FORCE
# Time: O(n! × n)  Space: O(n)
# Try all permutations of one array, check all pairs
from itertools import permutations
def isPossible_brute():
    a = [2, 1, 3]
    b = [7, 8, 9]
    k = 10
    for perm in permutations(b):
        valid = True
        for i in range(len(a)):
            if a[i] + perm[i] < k:
                valid = False
                break
        if valid:
            print(f"Brute Force Result: True")
            return

    print(f"Brute Force Result: False")
isPossible_brute()
