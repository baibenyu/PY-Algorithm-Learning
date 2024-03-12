# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/6 18:10'

import time
from collections import defaultdict
from collections import deque
from typing import List


class Solution(object):
    # 方法一:BFS
    def ladderLength(self, beginWord, endWord, wordList):
        # 建立通用list
        size, general_dic = len(beginWord), defaultdict(list)
        for w in wordList:
            for _ in range(size):  # 生成每一个单词能由哪些前缀单词变成的哈希表
                general_dic[w[:_] + "*" + w[_ + 1:]].append(w)
        # BFS
        queue = deque()
        queue.append((beginWord, 1))  # 因为在BFS中，queue中通常会同时混合多层的node，这就无法区分层了，要区分层就要queue中直接加入当前node所属层数。
        mark_dic = defaultdict(bool)  # bool 的默认值是false，因此所有不在list里的是false
        mark_dic[beginWord] = True
        while queue:
            cur_word, level = queue.popleft()  # queue头出来一个
            for i in range(size):  # 找邻居，这里的所有邻居都在level+1层
                for neighbour in general_dic[cur_word[:i] + "*" + cur_word[i + 1:]]:
                    if neighbour == endWord:
                        return level + 1
                    if not mark_dic[neighbour]:
                        mark_dic[neighbour] = True
                        queue.append((neighbour, level + 1))  # 符合条件（neighbour + unmarked)的进去
        return 0

    # 方法二:双向BFS--在明确已知起点和终点时,可以同时从两端进行BFS
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        l_queue = [beginWord]
        r_queue = [endWord]
        l_visited = set([beginWord])  # 不要 set(beginWord)
        r_visited = set([endWord])
        depth = 1

        while l_queue and r_queue:

            if len(l_queue) > len(r_queue):
                # 每次都走短的一侧，能走最小的面积
                l_queue, r_queue = r_queue, l_queue
                l_visited, r_visited = r_visited, l_visited

            # 如果写在range(len(l_queue))也行，因为只会计算第一次的长度，以后更新l_queue，range里面的值不会重新计算，但为了和其他语言兼容，这里写在外面比较好
            queue_sz = len(l_queue)
            for _ in range(queue_sz):  # 每层开始遍历
                cur = l_queue.pop(0)
                if cur in r_visited:  # 如果当前节点在另一侧走过，说明在这一层出现焦点了
                    return depth
                for i in range(len(beginWord)):  # 用26字母轮流喜欢替换单词每个位置的字母,直至找到处于字典中的单词组合
                    for j in range(97, 123):
                        n_node = cur[:i] + chr(j) + cur[i + 1:]
                        if n_node in wordSet and n_node not in l_visited:
                            l_queue.append(n_node)
                            l_visited.add(n_node)
            depth += 1

        return 0


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
