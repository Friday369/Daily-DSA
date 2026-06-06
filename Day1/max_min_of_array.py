# O(N) time complexity, O(1) space complexity
def find_max_min(arr):
    if not arr:
        return None, None  # Return None for both max and min if the array is empty

    max_value = arr[0]
    min_value = arr[0]

    for num in arr:
        if num > max_value:
            max_value = num
        elif num < min_value:
            min_value = num

    return max_value, min_value 
if __name__ == "__main__":
    arr=[3, 1, 4, 1, 5, 9, 2, 6, 5]
    max_value, min_value = find_max_min(arr)
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")