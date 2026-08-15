# OPTIMAL — HashMap + Two Pointer (right to left)
# Time: O(n)  Space: O(1)
def transform_optimal():
    s1 = "GeeksForGeeks"
    s2 = "ForGeeksGeeks"
    if len(s1) != len(s2):
        print("Optimal Result: -1")
        return
    freq = {}
    for c in s1:
        freq[c] = freq.get(c, 0) + 1
    for c in s2:
        freq[c] = freq.get(c, 0) - 1
    if any(v != 0 for v in freq.values()):
        print("Optimal Result: -1")
        return
    i = len(s1) - 1
    j = len(s2) - 1
    ops = 0

    while i >= 0 and j >= 0:
        if s1[i] == s2[j]:
            i -= 1
            j -= 1
        else:
            ops += 1
            i -= 1

    print(f"Optimal Result: {ops}")

transform_optimal()