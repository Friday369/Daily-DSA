class Solution:
    def areRotations(self, s1, s2):
        # code here
        if len(s1)!=len(s2):
            return False
        combined=s1+s1
        return s2 in combined