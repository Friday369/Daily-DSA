# BRUTE FORCE
# Time: O(n * m)  Space: O(n)
def mobileKeypad_brute():
    sentence = "GEEKSFORGEEKS"
    # map each letter to its keypad sequence
    keypad = {}
    keys = [
        "2", "22", "222",
        "3", "33", "333",
        "4", "44", "444",
        "5", "55", "555",
        "6", "66", "666",
        "7", "77", "777", "7777",
        "8", "88", "888",
        "9", "99", "999", "9999"
    ]
    for i, seq in enumerate(keys):
        keypad[chr(ord('A') + i)] = seq
    result = ""
    for c in sentence:
        if c == ' ':
            result += "0"
        else:
            result += keypad[c]          # O(m) lookup per char
    print(f"Brute Force Result: {result}")
mobileKeypad_brute()
