class Solution:
    def areAnagrams(self, s1, s2):
       # code here
       if len(s1)!=len(s2):
           return False
       count={}
       for c in s1:
           count[c]=count.get(c,0)+1
       for c in s2:
           count[c]=count.get(c,0)-1
       return all(v==0 for v in count.values())