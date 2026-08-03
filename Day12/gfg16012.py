class Solution:
    def maxCircularSum(self, arr):
        # code here
        n=len(arr)
        total=sum(arr)
        max_sum=arr[0]
        curr_max=arr[0]
        for i in range(1,n):
            curr_max=max(arr[i],curr_max+arr[i])
            max_sum=max(max_sum,curr_max)
        min_sum=arr[0]
        curr_min=arr[0]
        for i in range(1,n):
            curr_min=min(arr[i],curr_min+arr[i])
            min_sum=min(min_sum,curr_min)
        if total==min_sum:
            return max_sum
        return max(max_sum,total-min_sum)
        