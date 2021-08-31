class LinkNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def kmp(self, string) -> list:
        res = [0]
        size = len(string)
        left = 0
        right = 1
        for i in range(1, size - 1):
            right = i
            while left < right:
                if string[left] != string[right]:
                    break
                left += 1
                right -= 1
            res.append(left)
            left = 0
        return res

    def removeOccurrences(self, s: str, part: str) -> str:
        # 为part构造自动机(数组)
        machine = self.kmp(part)
        s_head = LinkNode(s[0])
        last = s_head
        index = 0
        if s[0] == part[0]:
            index += 1
        for i in range(1, len(s)):
            if s[i] == part[index]:
                index += 1
            else:
                pass
            last.next = LinkNode(s[i])
            last = last.next


if __name__ == "__main__":
    Solution().kmp("ABCDABD")