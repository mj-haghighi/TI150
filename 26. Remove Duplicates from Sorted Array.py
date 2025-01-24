# Beats70.27%
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        index = 0
        length = len(nums)
        last_unique = None

        while i < length:
            if nums[i] != last_unique:
                last_unique = nums[i]
                nums[index] = nums[i]
                index += 1
            i += 1
        return index
