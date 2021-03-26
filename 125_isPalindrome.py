# 使用双指针
class Solution:
    # def __init__(self):
    #     self.signal = {0,1,2,3,4,5,6,7,8,9}

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while(left <= right):
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].upper() != s[right].upper():
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    Solution().isPalindrome("A man, a plan, a canal: Panama")
