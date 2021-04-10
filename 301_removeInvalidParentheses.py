from typing import List


class Solution:
    def __init__(self):
        self.map = dict()
        self.s = ""
        self.maxSize = -1

    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 使用栈+回溯法
        self.s = s
        self.solve("", 0, 0, 0)
        return list(self.map[self.maxSize])

    def solve(self, stack, left, right, index):
        while(index < len(self.s)):
            _right = right
            _left = left
            if(self.s[index] == "("):
                _left += 1
            elif(self.s[index] == ")"):
                _right += 1
            else:
                stack += self.s[index]
                index += 1
                continue
            if(_left >= _right):
                self.solve(stack + self.s[index], _left, _right, index + 1)
                self.solve(stack, left, right, index + 1)
                return
            else:
                index += 1
        if(left == right):
            size = len(stack)
            self.maxSize = max(self.maxSize, size)
            if(size not in self.map):
                self.map[size] = set()
            self.map[size].add(stack)


solution = Solution()
ret = solution.removeInvalidParentheses("(a)())()")
print(len(ret))
