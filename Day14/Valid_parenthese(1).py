# BRUTE FORCE
# Time: O(n²)  Space: O(n)
def isValid_brute():
    s = "([{}])"
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")

    print(f"Brute Force Result: {s == ''}")
isValid_brute()


