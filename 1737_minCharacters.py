class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        # 模拟遍历三种可能性
        # 前两种比较难实现
        # 错位比较,遍历?
        # 前两种:双指针法
        # 最后一种,加和比较
        # !此为第三种
        ret = float("inf")
        a_dp = [0 for i in range(26)]
        b_dp = [0 for i in range(26)]
        for s in a:
            a_dp[ord(s) - 97] += 1
        for s in b:
            b_dp[ord(s) - 97] += 1
        totalSize = len(a) + len(b)
        for i in range(26):
            ret = min(ret, totalSize - a_dp[i] - b_dp[i])
        # 开始前两种
        # ! 第一种
        plus_a = [a_dp[0]]
        plus_b = [b_dp[0]]
        for i in range(1, 26):
            plus_a.append(plus_a[-1] + a_dp[i])
            plus_b.append(plus_b[-1] + b_dp[i])
        for i in range(26 - 1):
            temp_a = plus_a[i] + (plus_b[-1] - plus_b[i])
            ret = min(totalSize - temp_a, ret)
            temp_b = plus_b[i] + (plus_a[-1] - plus_a[i])
            ret = min(totalSize - temp_b, ret)
        return ret


if __name__ == "__main__":
    Solution().minCharacters("abadaasawaasdwdwawdadsdawa",
                             "adwagaadgdadawasadawssdawadawasdaczwqasawagawasd")
