#Time Complexity: O(2^(m+n))  Space Complexity: O(m+n)
def wildcardMatch_brute(s, p, i=0, j=0):
    if i == len(s) and j == len(p):
        return True
    if j == len(p):
        return False
    if i == len(s):
        return all(p[k] == '*' for k in range(j, len(p)))
    if p[j] == '*':
        return wildcardMatch_brute(s, p, i, j+1) or wildcardMatch_brute(s, p, i+1, j)
    elif p[j] == '?' or p[j] == s[i]:
        return wildcardMatch_brute(s, p, i+1, j+1)
    else:
        return False
s = "baaabab"
p = "*****ba*****ab"
print(wildcardMatch_brute(s, p))