#Time complexity: O(n^2)  Space complexity: O(n)
def groupAnagrams_brute(strs):
    groups = []
    for word in strs:
        placed = False
        sorted_word = sorted(word)

        for group in groups:
            if sorted(group[0]) == sorted_word:
                group.append(word)
                placed = True
                break
        if not placed:
            groups.append([word])
    return groups
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams_brute(strs))