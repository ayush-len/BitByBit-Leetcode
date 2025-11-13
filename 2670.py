class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        diff=[]
        for i in range(n):
            l=len(set(nums[i+1:n]))
            m=len(set(nums[0:i+1]))
            diff+=[(m-l)]
        return diff
