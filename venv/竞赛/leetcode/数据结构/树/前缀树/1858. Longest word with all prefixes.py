# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/1 7:59'

import time
from typing import List


class Trie:

    def __init__(self):
        self.map = {}
        self.word = ""

    def insert(self, word):
        cur = self

        for ch in word:
            if ch not in cur.map:
                cur.map[ch] = Trie()
            cur = cur.map[ch]
        cur.word = word

    def search(self):
        result = []
        cur = self
        for ch in cur.map:
            self.dfs(cur.map[ch], result)
        return result

    def dfs(self, cur, result):  # 一路深搜,若某一个前缀没有end,说明中断,直接return
        if not cur.word:
            return

        result.append(cur.word)
        for ch in cur.map:
            self.dfs(cur.map[ch], result)


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        for word in words:
            root.insert(word)

        ans = root.search()
        ans.sort(key = lambda x: (-len(x), x))
        return ans[0] if ans else ""


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
