from typing import List


# class TreeNode:
#     def __init__(self, char):
#         self.char = char
#         self.next = [None for i in range(26)]
#         self.pres = None


# class TriTree:
#     pass


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 由于word字符数量过大,应该使用前缀树
        # 直接对表格制作字典树
        # 直接使用表格进行回溯
        self.m = len(board)
        self.n = len(board[0])
        self.dict = board
        ret = []
        self.table = [[] for i in range(26)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.table[ord(board[i][j]) - 97].append([i, j])
        for word in words:
            if(self.search(word)):
                ret.append(word)
        return ret

    def search(self, word):
        for pos in self.table[ord(word[0]) - 97]:
            visit = set()
            visit.add(self.getString(pos[0], pos[1]))
            if(self._search(word, 1, pos[0], pos[1], visit)):
                return True
        return False

    def _search(self, word, index, i, j, visit):
        # index表示这次要找的
        if(index >= len(word)):
            return True
        arr = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
        for item in arr:
            if item[0] > -1 and item[0] < self.m and item[1] > -1 and item[1] < self.n:
                if self.dict[item[0]][item[1]] != word[index]:
                    continue
                string = self.getString(item[0], item[1])
                if string not in visit:
                    visit.add(string)
                    if(self._search(word, index + 1, item[0], item[1], visit)):
                        return True
                    visit.remove(string)
        return False

    def getString(self, i, j):
        return str(i) + "," + str(j)


if __name__ == "__main__":
    ret = Solution().findWords([["a", "a"]],
                               ["aaa"])
    print(ret)
