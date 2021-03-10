class Solution(object):
    def isMatch(self, s, p):
        d = {}
        return self.dp(s, p, d)

    def dp(self, s, p, d):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if(s + "," + p in d):
            return d[s + "," + p]
        # 根据情况匹配
        # 从前往后匹配
        size_s = len(s)
        size_p = len(p)
        i, j = 0, 0
        while(size_s != i and size_p != j):
            # 分情况判断
            if s[i] == p[j]:
                # 是否还有"*"
                if(j + 1 >= size_p or p[j + 1] != "*"):
                    i += 1
                    j += 1
                    continue
                else:
                    # 此时还有"*"
                    d[s + "," + p] = self.dp(
                        s[i:], p[j + 2:], d) or self.dp(s[i + 1:], p[j:], d)
                    return d[s + "," + p]
            elif(p[j] == "."):
                # 是否还有"*"
                if(j + 1 < size_p and p[j + 1] == "*"):
                    if(j + 1 == size_p - 1):
                        # 当"*"为最后一个
                        d[s + "," + p] = True
                        return d[s + "," + p]
                    else:
                        d[s + "," + p] = self.dp(s[i:], p[j + 2:], d
                                                 ) or self.dp(s[i + 1:], p[j:], d)
                        return d[s + "," + p]
                    # 其他情况
                else:
                    # 不含"*"
                    i += 1
                    j += 1
                    continue
            elif(j + 1 < size_p and p[j + 1] == "*"):
                # 匹配不成功,只能使*重复0次
                j += 2
                continue
            d[s + "," + p] = False
            return d[s + "," + p]
        # 此时s和p其中一个匹配完毕
        if(size_p == j and size_s == i):
            d[s + "," + p] = True
        elif(size_s != i):
            d[s + "," + p] = False
        else:
            if (size_p - j) % 2 != 0:
                d[s + "," + p] = False
                return d[s + "," + p]
            # 从此开始一次确认*的存在
            while(size_p != j):
                if p[j + 1] != "*":
                    d[s + "," + p] = False
                    return d[s + "," + p]
                j += 2
            d[s + "," + p] = True
        return d[s + "," + p]


if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch("abbaaaabaabbcba", "a*.*ba.*c*..a*.a*."))
