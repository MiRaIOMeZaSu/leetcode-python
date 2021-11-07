class Solution:
    def countVowels(self, word: str) -> int:
        # 求出每个元音字母被子字符串包含的次数×
        # 存在重复!
        # 使用前缀和?
        specialChar = {'a', 'e', 'i', 'o', 'u'}
        last = 0
        arr = []
        for ch in word:
            arr.append(last + (1 if ch in specialChar else 0))
            last = arr[-1]
        # 开始查找?
        # 10^5
        # 使用加和
        last = 0
        ans = 0
        for i in range(len(word)):
            ans += arr[i] * (i + 1) - last
            last += arr[i]
        return ans


if __name__ == "__main__":
    Solution().countVowels("aba")
