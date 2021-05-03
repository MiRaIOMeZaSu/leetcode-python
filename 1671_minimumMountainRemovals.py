from typing import List
import bisect


def get_lis_len_arr(arr):
    lst = []
    ans = []
    for i in range(len(arr)):
        idx = bisect.bisect_left(lst, arr[i])
        if idx >= 0 and idx < len(lst):
            # 下面更新过程不会改变lst的长度,因而不会导致新入的最大arr[i]的ans[i]出现错误
            lst[idx] = arr[i]
            ans.append(idx + 1)
        else:
            lst.append(arr[i])
            ans.append(len(lst))

    return ans


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        arr1 = get_lis_len_arr(nums)
        arr2 = get_lis_len_arr(nums[::-1])

        max_val = 0
        n = len(nums)
        for i in range(1, n - 1):
            if arr1[i] > 1 and arr2[n - i - 1] > 1:
                max_val = max(max_val, arr1[i] + arr2[n - i - 1] - 1)
        return n - max_val


if __name__ == "__main__":
    Solution().minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1])
