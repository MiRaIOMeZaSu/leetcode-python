from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 选出三个即可
        ret = [False for i in range(3)]
        for triplet in triplets:
            flag = False
            temp = []
            for i in range(3):
                if triplet[i] < target[i]:
                    continue
                elif triplet[i] == target[i]:
                    flag = True
                    temp.append(i)
                else:
                    flag = False
                    break
            if flag:
                for index in temp:
                    ret[index] = True
        return ret[0] and ret[1] and ret[2]


if __name__ == "__main__":
    ret = Solution().mergeTriplets([[3, 1, 7], [1, 5, 10]],
                                   [3, 5, 7])
    print(ret)
