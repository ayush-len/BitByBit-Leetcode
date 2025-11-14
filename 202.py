class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b=[]
        while n!=1 and n not in b:
            b.append(n)
            s=0
            while n>0:
                s+=((n%10)**2)
                n//=10
            n=s
        return n==1
