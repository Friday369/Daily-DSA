# BRUTE FORCE
# Time: O(n³)  Space: O(1)
def countSubstrings_brute():
    s = "abc"
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                count += 1
    print(f"Brute Force Result: {count}")
countSubstrings_brute()


