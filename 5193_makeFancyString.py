class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""
        size = len(s)
        count = 0
        last = ""
        for i in range(size):
            if s[i] == last:
                if count >= 2:
                    continue
                count += 1
            else:
                last = s[i]
                count = 1
            result += s[i]
        return result

if __name__ == "__main__":
    Solution().makeFancyString("leeetcode")