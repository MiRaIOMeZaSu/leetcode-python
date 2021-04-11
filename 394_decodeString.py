class Solution:
    def decodeString(self, s: str) -> str:
        # 用两个栈来取代函数栈的作用
        strs = []
        times = []
        string = ""
        size = len(s)
        num = 0
        for i in range(size):
            c = s[i]
            if(c.isdigit()):
                a = int(c)
                num = num * 10 + a
            else:
                if(num != 0):
                    times.append(num)
                    num = 0
                if(c == "["):
                    strs.append(string)
                    string = ""
                elif(c == "]"):
                    # 这个时候应该做出栈操作
                    out = strs.pop()
                    time = times.pop()
                    string = out + time * string
                else:
                    string += c
        return string


solution = Solution()
solution.decodeString("100[leetcode]")
