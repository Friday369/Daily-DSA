# OPTIMAL — HashMap / Frequency Count
# Time: O(n)  Space: O(1) — at most 26 keys
def isAnagram_optimal():
    s = "anagram"
    t = "nagaram"
    if len(s) != len(t):
        print("Optimal Result: False")
        return
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1   
    for c in t:
        count[c] = count.get(c, 0) - 1   
    result = all(v == 0 for v in count.values())
    print(f"Optimal Result: {result}")
isAnagram_optimal()