# BRUTE FORCE — Include/Exclude every element
# Time: O(2^n)   Space: O(r) recursion depth
def combinations_brute(arr, r):
    n = len(arr)
    result = []
    data = []
    def helper(ind):
        if len(data) == r:
            result.append(data.copy())
            return
        if ind >= n:
            return  
        data.append(arr[ind])
        helper(ind + 1)
        data.pop() 
        helper(ind + 1)
    helper(0)
    return result
arr = [1, 2, 3, 4]
r = 2
print("Brute Force:", combinations_brute(arr, r))
