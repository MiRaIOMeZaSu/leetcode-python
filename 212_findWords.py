from typing import List


class TreeNode:
    def __init__(self, char='', key=-1):
        self.char = char
        self.key = key
        self.next = dict()
        self.isEnd = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 由于word字符数量过大,应该使用前缀树?
        # 为输入字符(要寻找的字符)构造前缀树
        # 树构造完毕后在进行遍历
        self.ret = []
        self.finded = set()
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.table = [[] for i in range(26)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.table[ord(board[i][j]) - 97].append([i, j])
        tree = TreeNode()
        # 先构造树
        for word in words:
            curr = tree
            for i in range(len(word)):
                key = ord(word[i]) - 97
                if(key not in curr.next):
                    curr.next[key] = TreeNode(word[i], key)
                curr = curr.next[key]
            curr.isEnd = True
        # 深度优先?广度优先?
        self.visit = set()
        for node in tree.next.values():
            for pos in self.table[node.key]:
                string = self.getString(pos[0], pos[1])
                visit = set()
                visit.add(string)
                self.solve(node.char, pos[0], pos[1], node, visit)
        return self.ret

    def solve(self, currWord, i, j, node, visit):
        if node.isEnd:
            if currWord not in self.visit:
                self.visit.add(currWord)
                self.ret.append(currWord)
        arr = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
        for item in arr:
            if item[0] > -1 and item[0] < self.m and item[1] > -1 and item[1] < self.n:
                key_str = self.board[item[0]][item[1]]
                key = ord(key_str) - 97
                if key in node.next:
                    v = self.getString(item[0], item[1])
                    if v not in visit:
                        visit.add(v)
                        self.solve(currWord + key_str,
                                   item[0], item[1], node.next[key], visit)
                        visit.remove(v)

    def getString(self, i, j):
        return str(i) + "," + str(j)


if __name__ == "__main__":
    ret = Solution().findWords([["a", "a"]],
                               ["aaa"])
    print(ret)
