# OPTIMAL — Vertical Scanning
# Time: O(n * m)  Space: O(1)
def longestCommonPrefix_optimal():
    strs = ["flower", "flow", "flight"]
    if not strs:
        print("Optimal Result: ''")
        return
    for i in range(len(strs[0])):        # iterate over chars of first string
        c = strs[0][i]
        for s in strs[1:]:               # check same position in all strings
            if i >= len(s) or s[i] != c:
                print(f"Optimal Result: '{strs[0][:i]}'")
                return
    print(f"Optimal Result: '{strs[0]}'")
longestCommonPrefix_optimal()