class Solution:
	def maxProduct(self,arr):
		# code here
		curr_max=curr_min=result=arr[0]
		for i in range(1,len(arr)):
		    num=arr[i]
		    if num<0:
		        curr_max,curr_min=curr_min,curr_max
		    curr_max=max(num,curr_max*num)
		    curr_min=min(num,curr_min*num)
		    result=max(result,curr_max)
		return result