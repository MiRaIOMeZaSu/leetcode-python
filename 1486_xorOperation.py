class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # 等差数组 - 每次都加2
        # 从start开始以2为步长的等差序列
        # 重点是异或!
        ret = start
        for i in range(1, n):
            num = start + i * 2
            ret ^= num
        return ret
