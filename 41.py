class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i=0
        while i<n:
            v=nums[i]
            if 0<v<=n and nums[v-1]!=v:
                ci=v-1
                nums[i],nums[ci]=nums[ci],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
