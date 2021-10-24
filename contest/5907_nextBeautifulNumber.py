class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # 使用递归法
        if n == 0:
            return 1
        s = str(n)
        if len(s) == 1:
            return 22
        if len(s) == 2:
            return 122 if n >= 22 else 22
        if len(s) == 3:
            if n < 221:
                # 安排1的位置即可
                for i in [122, 212, 221]:
                    if n < i:
                        return i
            elif n < 333:
                return 333
            else:
                return 1333
        if len(s) == 4:
            if n < 3331:
                # 安排1的位置即可
                for i in [1333, 3133, 3313, 3331]:
                    if n < i:
                        return i
            elif n < 4444:
                return 4444
            else:
                return 14444
        if len(s) == 5:
            if n < 44441:
                ans = float('inf')
                for arr in [[2, 3], [1, 4]]:
                    ans = min(ans, self.solve(arr, n))
                return ans
            elif n < 55555:
                return 55555
            else:
                return 122333
        if len(s) == 6:
            if n < 555551:
                ans = float('inf')
                for arr in [[1, 2, 3], [2, 4], [1, 5]]:
                    ans = min(ans, self.solve(arr, n))
                return ans
            elif n < 666666:
                return 666666
            else:
                return 1224444
        if len(s) == 7:
            return 1224444

    def solve(self, count: list, target: int):
        d = {}
        ans = [float('inf')]
        for i in count:
            d[i] = i
        self.process(d, 0, ans, target)
        return ans[0]

    def process(self, count: dict, curr: int, ans: list, target):
        if curr > target:
            ans[0] = min(ans[0], curr)
        for i in count.keys():
            if count[i] > 0:
                next = curr * 10 + i
                count[i] -= 1
                self.process(count, next, ans, target)
                count[i] += 1


if __name__ == "__main__":
    # 最长为6位
    # 1:1, 2:2,3:[1,2][3],4:[1,3][4],5:[2,3],[1,4],[5],6:[1,2,3],[2,4],[1,5],[6]
    print(Solution().nextBeautifulNumber(10461))
