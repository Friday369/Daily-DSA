# BRUTE FORCE — Simple Array
# Time: O(|b-a|)  Space: O(|b-a|)
# Use a regular array where each index = 0 or 1

def markMultiples_brute():
    a, b = 2, 10
    size = abs(b - a) + 1
    array = [0] * size          # one int per number = wasteful
    for i in range(a, b + 1):
        if i % 2 == 0 or i % 5 == 0:
            array[i - a] = 1    # mark as multiple
    print("Brute Force Result: ", end="")
    for i in range(a, b + 1):
        if array[i - a] == 1:
            print(i, end=" ")
    print()

markMultiples_brute()