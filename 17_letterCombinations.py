from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        # a-z一共26个,7和9有4个
        table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ret = [i for i in table[digits[0]]]
        temp = []
        for i in range(1, len(digits)):
            for e in table[digits[i]]:
                temp.extend([x + e for x in ret])
            ret = temp
            temp = []
        return ret


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
