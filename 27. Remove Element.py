class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        index = 0
        while i < len(nums):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
            i += 1

        return index
