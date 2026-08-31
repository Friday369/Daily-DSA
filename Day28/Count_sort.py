#Time Complexity: O(n+k)
#Space Complexity: O(n+k)
def countingSort_optimal(arr):
    if not arr:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    # count occurrences of each element
    for num in arr:
        count[num - min_val] += 1
    # build the sorted output by walking through counts in order
    output = []
    for i in range(range_of_elements):
        output.extend([i + min_val] * count[i]) 
    return output
arr = [4, 3, 12, 1, 5, 5, 3, 9]
print(countingSort_optimal(arr))