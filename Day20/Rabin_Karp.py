#Time Complexity: O(n + m) in average case, O(n*m) in worst case 
#Space Complexity: O(1)
def patternSearch_rabinKarp(text, pattern, q=101):
    d = 256  # number of characters in the input alphabet
    n = len(text)
    m = len(pattern)
    positions = []

    h = pow(d, m - 1) % q   # value of d^(m-1) % q, used for removing leading digit
    p_hash = 0               # hash value for pattern
    t_hash = 0                # hash value for current window of text

    # calculate initial hash values for pattern and first window of text
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for i in range(n - m + 1):
        # if hash values match, verify character by character (avoid false positives)
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                positions.append(i)

        # compute hash for next window: remove leading char, add trailing char
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q

    return positions

text = "AABAACAADAABAABA"
pattern = "AABA"
print(patternSearch_rabinKarp(text, pattern))