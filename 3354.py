class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=[]  
        c=0
        d=0      
        for i in range(len(nums)):
            if nums[i]==0:
                b.append(i)
        for j in b:
            s1=sum(nums[0:j])
            s2=sum(nums[j:len(nums)])
            if s1==s2:
                c+=1
            elif abs(s1-s2)==1:
                d+=1
        return (c*2 + d)
