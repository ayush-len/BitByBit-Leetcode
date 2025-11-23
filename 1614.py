class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        l=[]
        for i in s:
            if i=="(":
                c+=1
                l+=[c]
            if i==")":
                c-=1
        if len(l)==0:
            return 0
        else:
            return max(l)
