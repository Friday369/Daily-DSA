# BRUTE FORCE
# Time: O(n * m²)  Space: O(m)
def longestCommonPrefix_brute():
    strs = ["flower", "flow", "flight"]
    if not strs:
        print("Brute Force Result: ''")
        return
    prefix = strs[0]
    for s in strs[1:]:
        # shrink prefix until s starts with it
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                print("Brute Force Result: ''")
                return
    print(f"Brute Force Result: '{prefix}'")
longestCommonPrefix_brute()


