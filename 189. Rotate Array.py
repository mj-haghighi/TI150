class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        last_k_elements = nums[-k:]

        last_i = len(nums) - k - 1
        while last_i >= 0:
            nums[last_i + k] = nums[last_i]
            last_i -= 1

        for i, e in enumerate(last_k_elements):
            nums[i] = e
