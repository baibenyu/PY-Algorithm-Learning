# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/1 8:19'

import time
from collections import defaultdict
from typing import List


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(now, i1, j1):  # 针对每一个坐标的字母深搜检查是否位于前缀树中
            if board[i1][j1] not in now.children:
                return

            ch = board[i1][j1]

            now = now.children[ch]
            if now.word != "":
                ans.add(now.word)

            board[i1][j1] = "#"
            for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    dfs(now, i2, j2)
            board[i1][j1] = ch

        trie = Trie()
        for word in words:  # 针对每一个可能成为ans中的单词建前缀树
            trie.insert(word)

        ans = set()
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return list(ans)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
