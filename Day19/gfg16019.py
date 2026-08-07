class Solution:
    def minChar(self, s):
        # code here
        n=len(s)
        combined=s+'#'+s[::-1]
        m=len(combined)
        lps=[0]*m
        length=0
        i=1
        while i<m:
            if combined[i]==combined[length]:
                length+=1
                lps[i]=length
                i+=1
            elif length!=0:
                length=lps[length-1]
            else:
                lps[i]=0
                i+=1
        longest_palindromic_prefix=lps[m-1]
        return n-longest_palindromic_prefix