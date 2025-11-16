class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        m=0
        for n,s,e in trips:
            if e>m:
                m=e
        t=[0]*(m+1)
        for n,s,e in trips:
            t[s]+=n
            if e<=m:
                t[e]-=n
        p=0
        for i in t:
            p+=i
            if p>capacity:
                return False
        return True
