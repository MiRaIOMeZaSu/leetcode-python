from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = []
        for s in nums:
            arr.append(int(s))
        arr.sort(reverse=True)
        return str(arr[k - 1])


if __name__ == "__main__":
    Solution().kthLargestNumber(["3", "6", "7", "10"],
                                4)
