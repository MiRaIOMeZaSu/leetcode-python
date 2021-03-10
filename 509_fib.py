class Solution(object):
    # 使用dp table 记录
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [-1 for i in range(n + 1)]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif dp[n] != -1:
            return dp[-1]
        # 此处,教程答案提前将dp表先在for循环中填满,最后再提供答案
        return self.fib(n - 1) + self.fib(n - 2)
