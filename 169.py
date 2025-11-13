class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n1=set(nums)
        n=len(nums)
        for i in n1:
            c=nums.count(i)
            if c>(n/2):
                return i
