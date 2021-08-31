from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        # 突变的是一个子字符串
        # 选择最前的即可5
        start = ""
        end = ""
        sub_str = ""
        for index in range(len(num)):
            i = int(num[index])
            if change[i] > i:
                sub_str += str(change[i])
                start = num[:index]
                # 此时往后找直到不满足
                for j in range(index + 1, len(num)):
                    i = int(num[j])
                    if change[i] < i:
                        end = num[j:]
                        break
                    sub_str += str(change[i])
                break
        if not sub_str:
            return num
        return start + sub_str + end


if __name__ == "__main__":
    result = Solution().maximumNumber("00001472194",[9,3,6,3,7,3,1,4,5,8])
    print(result)