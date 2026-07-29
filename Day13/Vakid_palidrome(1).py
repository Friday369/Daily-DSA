# BRUTE FORCE
# Time: O(n)  Space: O(n)

def isPalindrome_brute():
    s = "A man, a plan, a canal: Panama"
    cleaned = ""
    for c in s:
        if c.isalnum():
            cleaned += c.lower()
    result = cleaned == cleaned[::-1]
    print(f"Brute Force Result: {result}")

isPalindrome_brute()


