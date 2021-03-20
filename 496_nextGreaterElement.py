from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for index in range(0, len(nums1)):
            for i in nums2[nums2.index(nums1[index]) + 1:]:
                if(nums1[index] < i):
                    result.append(i)
                    break
            if(len(result) != index + 1):
                result.append(-1)
        # 输入了两个数组
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreaterElement([4], [1, 2, 3, 4]))
