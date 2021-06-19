class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        ret = ""
        for i in range(len(arr) - 1, -1, -1):
            if len(arr[i]) == 0:
                continue
            if(len(ret) != 0):
                ret += " "

            ret += arr[i]
        return ret


if __name__ == "__main__":
    Solution().reverseWords("  hello world  ")
