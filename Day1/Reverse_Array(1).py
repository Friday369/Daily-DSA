#O(N) time complexity, O(1) space complexity
def reversearray(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
if __name__ == "__main__":
    arr=[1,2,3,4,5]
    reversearray(arr)
    print(arr)
    for i in range(len(arr)):
           
           print(arr[i],end=" ")