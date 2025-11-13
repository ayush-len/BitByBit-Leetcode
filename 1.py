class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in set(nums):
            j=target-i
            if i==j:
                f=nums.index(i)
                nums.pop(f)
                if j not in nums:
                    continue
                elif j in nums:
                    s=nums.index(j)
                    return [f,s+1]
                
            elif i!=j:
                if j in nums:
                    f=nums.index(i)
                    s=nums.index(j)
                    if f!=s:
                        return [f,s]
