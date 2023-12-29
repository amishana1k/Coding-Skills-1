#Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        r=0
        for i in range(1,n):
                if nums[r]!=nums[i]:
                    r+=1
                    nums[r]=nums[i]
        return r+1
