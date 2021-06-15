from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        size = len(arr)
        right = size - 1
        while left < right:
            mid = (left + right) >> 1
            if mid == size - 1:
                return mid
            elif arr[mid + 1] > arr[mid]:
                left = mid + 1
            elif mid == 0:
                return mid
            elif arr[mid - 1] > arr[mid]:
                right = mid - 1
            else:
                return mid
        return left


if __name__ == "__main__":
    Solution().peakIndexInMountainArray([3, 5, 3, 2, 0])
