class Solution:
    def inversionCount(self, arr):
        def mergeSortAndCount(arr,left,right):
            count=0
            if left<right:
                mid=(left+right)//2
                count+=mergeSortAndCount(arr,left,mid)
                count+=mergeSortAndCount(arr,mid+1,right)
                count+=mergeAndCount(arr,left,mid,right)
            return count
        def mergeAndCount(arr,left,mid,right):
            leftArr=arr[left:mid+1]
            rightArr=arr[mid+1:right+1]
            i=j=0
            k=left
            count=0
            while i<len(leftArr) and j<len(rightArr):
                if leftArr[i]<=rightArr[j]:
                    arr[k]=leftArr[i]
                    i+=1
                else:
                    arr[k]=rightArr[j]
                    count+=(len(leftArr)-i)
                    j+=1
                k+=1
            
            while i<len(leftArr):
                arr[k]=leftArr[i]
                i+=1
                k+=1
            while j<len(rightArr):
                arr[k]=rightArr[j]
                j+=1
                k+=1
            return count
        return mergeSortAndCount(arr,0,len(arr)-1)
            
            
            
        # code here
        
            
            
            