# Beats32.27%
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
        seen_flag = False

        while i < length:
            if nums[i] != last_unique:
                last_unique = nums[i]
                nums[index] = nums[i]
                index += 1
                seen_flag = False

            elif nums[i] == last_unique and seen_flag == False:
                last_unique = nums[i]
                nums[index] = nums[i]
                index += 1
                seen_flag = True
            i += 1
        return index
