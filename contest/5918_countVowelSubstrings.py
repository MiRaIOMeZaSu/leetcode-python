class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        d = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        target = 1 + 2 + 4 + 8 + 16
        curr = 0
        ans = 0
        for i in range(len(word)):
            if word[i] in d:
                curr |= d[word[i]]
            else:
                ans += target == curr if 1 else 0
                curr = 0
        ans += target == curr if 1 else 0
        return ans


if __name__ == "__main__":
    Solution().countVowelSubstrings()
