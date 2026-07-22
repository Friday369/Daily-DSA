# OPTIMAL — Bit Manipulation
# Time: O(|b-a|)  Space: O(|b-a| / 32)
# Pack 32 flags into a single integer instead of 1 per index
import math
def checkbit(array, index):
    return array[index >> 5] & (1 << (index & 31))  
def setbit(array, index):
    array[index >> 5] |= (1 << (index & 31))
def markMultiples_optimal():
    a, b = 2, 10
    size = math.ceil(abs(b - a) / 32)   # 32x fewer slots needed!
    array = [0] * size
    for i in range(a, b + 1):
        if i % 2 == 0 or i % 5 == 0:
            setbit(array, i - a)
    print("Optimal Result: ", end="")
    for i in range(a, b + 1):
        if checkbit(array, i - a):
            print(i, end=" ")
    print()
markMultiples_optimal()