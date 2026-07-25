# BRUTE FORCE
# Time: O(n)  Space: O(n)
def isPalindrome_brute():
    s = "A man, a plan, a canal: Panama"
    cleaned = ""
    for c in s:
        if c.isalnum():
            cleaned += c.lower()
    print(f"Brute Force Result: {cleaned == cleaned[::-1]}")
isPalindrome_brute()

