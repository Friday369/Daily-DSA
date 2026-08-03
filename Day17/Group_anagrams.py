#Time complexity: O(nklogk)  Space complexity: O(nk)
def groupAnagrams_optimal(strs):
    groups = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams_optimal(strs))