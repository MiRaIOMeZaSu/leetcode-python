from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 使用插入排序
        for i in range(0, n):
            nums1[m + i] = nums2[i]
        if(m == 0):
            return
        # 以已排序序列长度为m开始使用插入排序
        for i in range(m, len(nums1)):
            _new = nums1[i]
            j = 0
            while(nums1[i - 1 - j] > _new and i - 1 - j >= 0):
                nums1[i - j] = nums1[i - 1 - j]
                j += 1
            nums1[i - j] = _new


if __name__ == "__main__":
    Solution().merge([4, 5, 6, 0, 0, 0],
                     3,
                     [1, 2, 3],
                     3)
