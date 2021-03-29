class Solution:
    def solve(self, nums):
        # 直接找出所有连续递增序列的开头和结尾下标
        if(len(nums) <= 1):
            return len(nums)
        indexs = [[0, -1]]
        pivot = nums[0]
        lengthes = []
        _max = -1
        for i in range(1, len(nums)):
            if nums[i] <= pivot:
                indexs[len(indexs) - 1][1] = i - 1
                indexs.append([i, -1])
                temp = indexs[len(indexs) - 2][1] - \
                    indexs[len(indexs) - 2][0] + 1
                if temp > _max:
                    _max = temp
                lengthes.append(temp)
            pivot = nums[i]
        indexs[len(indexs) - 1][1] = len(nums) - 1
        temp = indexs[len(indexs) - 1][1] - indexs[len(indexs) - 1][0] + 1
        _max = temp if temp > _max else _max
        lengthes.append(len(nums) - 1 - indexs[len(indexs) - 1][0] + 1)
        for i in range(1, len(lengthes)):
            if lengthes[i] > 1:
                if nums[indexs[i - 1][1]] < nums[indexs[i][0] + 1]:
                    temp = lengthes[i - 1] + lengthes[i] - 1
                    _max = temp if temp > _max else _max
                elif lengthes[i - 1] > 1:
                    if nums[indexs[i - 1][1] - 1] < nums[indexs[i][0]]:
                        temp = lengthes[i - 1] + lengthes[i] - 1
                        _max = temp if temp > _max else _max
        return _max


if __name__ == "__main__":
    print(Solution().solve(nums=[0, 3, 1, 2]))
