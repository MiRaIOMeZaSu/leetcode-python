from typing import List


class Solution:
    def __init__(self):
        self.ret = set()

    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 每次不满足时都必须在前面的序列中删除一个括号
        # 要求删除的数量最少
        # 最后的结果,从反方向再进行一次?
        # 第一次时删除的括号数量相同,因此相反时,应该删除的括号数也会相同
        size = len(s)
        self.solve(0, size, s, 0, 0, 0)
        temp = self.ret
        self.ret = set()
        for i in temp:
            self.solve(len(i) - 1, -1, i, 0, 0, 0)
        return list(self.ret)

    def solve(self, index, end, s, left, right, deled):
        if(left + right == len(s)):
            self.ret.add(s)
            return
        flag = index < end
        step = 1 if index < end else -1
        lefts = []
        rights = []
        for i in range(index, end, step):
            if(s[i] == '('):
                left += 1
                lefts.append(i)
            elif(s[i] == ')'):
                right += 1
                rights.append(i)
            else:
                continue
            if(left == right):
                continue
            if((left < right and flag) or (left > right and not flag)):
                toHandle = []
                if(flag):
                    # 正序
                    toHandle = rights
                else:
                    toHandle = lefts
                last = -10
                for todel in toHandle:
                    if(todel == last + step):
                        continue
                    _s = s[:todel] + s[todel + 1:]
                    _i = len(_s) - left - \
                        right if not flag else left + right - 1
                    if(_i >= len(_s)):
                        _i -= 1
                    self.solve(_i, -1 if not flag else len(_s), _s,
                               left if flag else left - 1, right if not flag else right - 1, deled + 1)

                    last = todel
                return
        self.ret.add(s)


solution = Solution()
solution.removeInvalidParentheses("()())())())(((()()(")
