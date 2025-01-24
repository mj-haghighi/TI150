class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        t = int(length / 2) + 1
        storage = {}
        for num in nums:
            if num in storage.keys():
                storage[num] += 1
            else:
                storage[num] = 1

        for num, counts in storage.items():
            if counts >= t:
                return num
