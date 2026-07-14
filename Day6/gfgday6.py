class Solution:
    def findMajority(self,arr):
        n=len(arr)
        cand1,cand2=None,None
        freq1,freq2=0,0
        for num in arr:
            if num==cand1:
                freq1+=1
            elif num==cand2:
                freq2+=1
            elif freq1==0:
                cand1,freq1=num,1
            elif freq2==0:
                cand2,freq2=num,1
            else:
                freq1-=1
                freq2-=1
        freq1,freq2=0,0
        for num in arr:
            if num==cand1:
                freq1+=1
            if num==cand2:
                freq2+=1
        result=[]
        if freq1>n//3:
            result.append(cand1)
        if freq2>n//3:
            result.append(cand2)
        return sorted(result)
                 