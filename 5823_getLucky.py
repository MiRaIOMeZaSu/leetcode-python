class Solution:
    def getLucky(self, s: str, k: int) -> int:
        pivot = ord('a') - 1
        num = ""
        for c in s:
            num += str(ord(c) - pivot)
        count = 0
        for i in range(k):
            count = 0
            for n in num:
                count += int(n)
            num = str(count)
        return count

        
if __name__ == "__main__":
    Solution().getLucky("leetcode",2)