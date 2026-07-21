# BRUTE FORCE
# Time: O(n²)  Space: O(n)
# Try all possible merge combinations recursively

def minMerges_brute():
    arr = [1, 4, 5, 1]

    def solve(a):
        left, right = 0, len(a) - 1
        ops = 0
        a = a[:]

        while left < right:
            if a[left] == a[right]:
                left += 1
                right -= 1
            elif a[left] < a[right]:
                a[left + 1] += a[left]   # merge left two
                left += 1
                ops += 1
            else:
                a[right - 1] += a[right]  # merge right two
                right -= 1
                ops += 1

        return ops

    print(f"Brute Force Result: {solve(arr)}")

minMerges_brute()


