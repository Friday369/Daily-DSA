# OPTIMAL — Stack
# Time: O(n)  Space: O(n)
def isValid_optimal():
    s = "([{}])"
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in mapping:                          
            if not stack or stack[-1] != mapping[c]:
                print("Optimal Result: False")
                return
            stack.pop()
        else:
            stack.append(c)                       
    print(f"Optimal Result: {len(stack) == 0}")
isValid_optimal()