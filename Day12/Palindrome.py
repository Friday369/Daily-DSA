# OPTIMAL — Two Pointer
# Time: O(n)  Space: O(1)
# No extra string, compare from both ends in place
def isPalindrome_optimal():
    s = "A man, a plan, a canal: Panama"
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            print("Optimal Result: False")
            return
        left += 1
        right -= 1
    print("Optimal Result: True")
isPalindrome_optimal()