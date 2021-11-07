class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # 使用简单的遍历法
        # 前缀法?
        alp = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        target = 1 + 2 + 4 + 8 + 16
        ans = 0
        for i in range(len(word)):
            bit = 0
            d = dict()
            for ch in 'aeiou':
                d[ch] = 0
            total = 0
            for j in range(i, len(word)):
                # 使用计数
                if word[j] in alp:
                    bit |= alp[word[j]]
                total += 1
                d.setdefault(word[j], 0)
                d[word[j]] += 1
                temp = 0
                for ch in 'aeiou':
                    temp += d[ch]
                if total > temp:
                    break
                elif bit == target:
                    ans += 1
        return ans


if __name__ == "__main__":
    Solution().countVowelSubstrings("aeiouu")
