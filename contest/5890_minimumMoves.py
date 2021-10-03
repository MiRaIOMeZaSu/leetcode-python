class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = 0
        index = 0
        size = len(s)
        s = [s[i] for i in range(len(s))]
        while index < size:
            if s[index] == 'X':
                ans += 1
                for i in range(index, min(index + 3, size)):
                    s[i] = 'O'
                index = index + 3
                continue
            index += 1
        return ans


if __name__ == "__main__":
    Solution().minimumMoves("XXOX")
