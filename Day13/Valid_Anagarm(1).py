# BRUTE FORCE
# Time: O(n log n)  Space: O(n)
# Sort both strings and compare
def isAnagram_brute():
    s = "anagram"
    t = "nagaram"
    result = sorted(s) == sorted(t)
    print(f"Brute Force Result: {result}")
isAnagram_brute()
