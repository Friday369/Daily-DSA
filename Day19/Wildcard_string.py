#Time Complexity: O(n*m)  Space Complexity: O(m)
def wildcardMatch_optimized(s, p):
    n, m = len(s), len(p)
    prev = [False] * (m + 1)
    prev[0] = True

    for j in range(1, m + 1):
        if p[j-1] == '*':
            prev[j] = prev[j-1]

    for i in range(1, n + 1):
        curr = [False] * (m + 1)
        for j in range(1, m + 1):
            if p[j-1] == '*':
                curr[j] = curr[j-1] or prev[j]
            elif p[j-1] == '?' or p[j-1] == s[i-1]:
                curr[j] = prev[j-1]
        prev = curr

    return prev[m]
s = "baaabab"
p = "*****ba*****ab"
print(wildcardMatch_optimized(s, p))