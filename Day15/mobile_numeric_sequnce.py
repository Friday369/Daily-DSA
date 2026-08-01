# OPTIMAL — Index Math (no explicit map)
# Time: O(n)  Space: O(1)
# Use position arithmetic instead of building a dictionary
def mobileKeypad_optimal():
    sentence = "GEEKSFORGEEKS"
    # S and Z take 4 presses, rest take position+1 presses
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
    result = ""
    for c in sentence:
        if c == ' ':
            result += "0"
        else:
            result += keys[ord(c) - ord('A')]   # direct index, O(1)
    print(f"Optimal Result: {result}")
mobileKeypad_optimal()