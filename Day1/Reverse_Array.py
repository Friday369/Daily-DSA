#Brute Force Approach: By creating a temporary array and filling it with elements from the original array in reverse order, we can reverse the array. This approach has a time complexity of O(n) and a space complexity of O(n) due to the additional temporary array used for storing the reversed elements.
def reversearray(arr):
    n=len(arr)
    temp=[0]*n

    for i in range(n):
        temp[i]=arr[n-1-i]
    for i in range(n):
        arr[i]=temp[i]
if __name__ == "__main__":
    arr=[1,2,3,4,5]
    reversearray(arr)
    print(arr)
