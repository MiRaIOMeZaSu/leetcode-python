class Solution:
    def nthUglyNumber(self, n: int) -> int:
        n = n - 1
        if(n == 0):
            return 1
        list1 = []
        start = 2
        for i in range(n):
            list1.append(start)
            start *= 2
        for num in [3, 5]:
            list2 = []
            for i in range(n):
                list2.append(num)
                num *= 2
            list3 = []
            self.getNums(list1, list2, list3, n)
            list1 = list3
        pivot = 0
        while(pivot != 3):
            pivot = 0
            for i in [5, 3, 2]:
                list2 = [num * i for num in list1]
                list3 = []
                pivot += 1 if not self.getNums(list1, list2, list3, n) else 0
                list1 = list3
        return list1[-1]

    def getNums(self, list1, list2, ret, k):
        flag = False
        p1 = 0
        p2 = 0
        while(len(ret) < k and p2 < k and p1 < k):
            if(list1[p1] > list2[p2]):
                if(len(ret) == 0 or (len(ret) > 0 and ret[-1] != list2[p2])):
                    ret.append(list2[p2])
                p2 += 1
            else:
                if(len(ret) == 0 or (len(ret) > 0 and ret[-1] != list1[p1])):
                    ret.append(list1[p1])
                p1 += 1
        if(list1[0] != ret[0] or list1[-1] != ret[-1]):
            flag = True
        return flag


solution = Solution()
solution.nthUglyNumber(2)
