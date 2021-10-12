import sys

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # print(float('inf'))
        # print(sys.maxsize)
        ans = 0
        # 被除数和除数均为 32 位有符号整数。
        # 除数不为 0。
        # 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
        # 要求不使用乘法、除法和 mod 运算符
        isPositive = True
        if dividend < 0:
            isPositive = not isPositive
            dividend = - dividend
        elif dividend ==0:
            return 0
        if divisor < 0:
            isPositive = not isPositive
            divisor = - divisor
        elif divisor ==0:
            return 0
        index = 0
        if divisor > dividend:
            return 0
        elif dividend==divisor:
            return 1 if isPositive else -1
        ans = 0
        arr = [0,divisor]
        index = [0,1]
        # 0,1,2,4,8,16....
        while arr[-1] < dividend:
            arr.append(arr[-1] + arr[-1])
            index.append(index[-1] + index[-1])
        for i in range(len(arr) - 1,0,-1):
            if dividend >= arr[i]:
                dividend -= arr[i]
                ans += index[i]
        ans = ans if isPositive else -ans
        if ans >= 2147483648:
            ans -= 1
        return ans
        
if __name__ == "__main__":
    print(Solution().divide(-2147483648,1))