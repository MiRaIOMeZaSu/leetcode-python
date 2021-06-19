from typing import List


class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        maxI = max(questions)
        size = len(questions)
        pivot = size >> 1
        arr = [0 for i in range(maxI + 1)]
        for i in questions:
            arr[i] += 1
        arr.sort()
        num = 0
        index = 0
        for i in range(len(arr) - 1, -1, -1):
            index += 1
            num += arr[i]
            if num >= pivot:
                return index
        return index


if __name__ == "__main__":
    ret = Solution().halfQuestions([1, 5, 1, 3, 4, 5, 2, 5, 3, 3, 8, 6])
