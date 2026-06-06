#Brute Force Approach
def find_max_min(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[-1], sorted_arr[0]  # Return max and min from the sorted array
if __name__ == "__main__":
    arr=[3,1,2,4,1,9,5,6,5]
    result = find_max_min(arr)
    print(f"Maximum value: {result[0]}")
    print(f"Minimum value: {result[1]}")
    