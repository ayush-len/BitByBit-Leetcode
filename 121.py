class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        mp=0
        minp=prices[0] 
        for price in prices[1:]:
            cp=price-minp
            if cp>mp:
                mp=cp
            if price<minp:
                minp=price
        return mp
