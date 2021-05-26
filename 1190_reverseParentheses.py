class Solution:
    def reverseParentheses(self, s: str) -> str:
        # 使用栈
        self.s = s
        self.size = len(s)
        return self.solve(0)

    def solve(self, index) -> list:
        def getStack(stack: list):
            temp = ""
            for j in range(len(stack) - 1, -1, -1):
                for x in range(len(stack[j]) - 1, -1, -1):
                    temp += stack[j][x]
            return temp
        stack = []
        i = index
        while i < self.size:
            # for i in range(index, self.size):
            if self.s[i] == "(":
                temp = self.solve(i + 1)
                stack.append(temp[0])
                i = temp[1]
                continue
            elif self.s[i] == ")":
                return [getStack(stack), i + 1]
            else:
                stack.append(self.s[i])
            i += 1
        ret = ""
        for string in stack:
            ret += string
        return ret


if __name__ == "__main__":
    ret = Solution().reverseParentheses("(u(love)i)")
    print(ret)
