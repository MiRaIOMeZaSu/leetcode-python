class Solution(object):
    def coinChange(self, coins, amount):
        # 通过一个dp table记录每个amount需要的最小coin数量
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0
        for i in range(0, len(dp)):
            for coin in coins:
                if i < coin:
                    continue
                
                # if temp >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])
        # print(dp)
        return -1 if dp[amount] == amount + 1 else dp[amount]


if __name__ == "__main__":
    solut = Solution()
    print(solut.coinChange([1, 2, 5], 11))
    print(solut.coinChange([2], 3))
