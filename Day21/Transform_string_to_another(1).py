# BRUTE FORCE
# Time: O(n²)  Space: O(n)
def transform_brute():
    s1 = "GeeksForGeeks"
    s2 = "ForGeeksGeeks"
    if len(s1) != len(s2):
        print("Brute Force Result: -1 (different lengths)")
        return
    # check if anagram
    if sorted(s1) != sorted(s2):
        print("Brute Force Result: -1 (not anagrams)")
        return
    s1 = list(s1)
    ops = 0
    n = len(s1)
    for j in range(n - 1, -1, -1):
        if s1[n - 1] != s2[j]:
            # find s2[j] in s1 and move to front
            for i in range(n):
                if s1[i] == s2[j]:
                    s1.pop(i)
                    s1.insert(0, s2[j])
                    ops += 1
                    break
    print(f"Brute Force Result: {ops}")
transform_brute()


