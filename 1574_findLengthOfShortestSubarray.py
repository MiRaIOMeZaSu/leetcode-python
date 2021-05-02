from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # 动态规划
        # 只能删除!一个!子数组
        # 由于只能删除一个数字,要么留前缀,要么留后缀,要么留的是某长度的前缀以及某长度的后缀
        # 先探测出适合的前缀和后缀
        last = arr[0]
        pre = 1
        for i in range(1, len(arr)):
            if(arr[i] >= last):
                pre += 1
            else:
                break
            last = arr[i]
        tail = 1
        last = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            if(arr[i] <= last):
                tail += 1
            else:
                break
            last = arr[i]
        # 此时开始双指针
        ret = max(pre, tail)
        if (pre + tail) <= len(arr) and arr[pre - 1] <= arr[-tail]:
            return len(arr) - (pre + tail)
        if pre == len(arr):
            return 0
        # 开始
        left = 0
        right = len(arr) - tail
        while(left <= pre - 1):
            while(right < len(arr) and arr[right] < arr[left]):
                right += 1
            if right >= len(arr):
                return len(arr) - ret
            ret = max(ret, left + 1 + (len(arr) - right))
            left += 1
        return len(arr) - ret


if __name__ == "__main__":
    Solution().findLengthOfShortestSubarray([])
