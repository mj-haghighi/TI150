class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index_1 = 0
        index_2 = 0

        len_1 = m
        len_2 = n

        res = []
        while index_1 < len_1 or index_2 < len_2:
            if index_2 >= len_2 or (
                index_1 < len_1 and nums1[index_1] < nums2[index_2]
            ):
                res.append(nums1[index_1])
                index_1 += 1
            else:
                res.append(nums2[index_2])
                index_2 += 1

        for i, n in enumerate(res):
            nums1[i] = n
