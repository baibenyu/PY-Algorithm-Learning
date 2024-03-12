# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/17 17:39'

import time
from collections import defaultdict
from collections import deque
import heapq


class TrieNode:
    def __init__(self, is_word=False, count=0):
        self.count = count  # 用来存当前word被查询过的次数，默认为0
        self.word = ""  # 用来存当前节点代表的word，默认为空，也就是不是单独的word
        self.next = defaultdict(TrieNode)  # 用来存下一个字母对应的节点

    def insert(self, word, time):  # 将word插入到当前的节点中
        curr = self
        for ch in word:
            curr = curr.next[ch]  # 用了defaultdict，所以不用做其它的判断初始化之类的

        curr.word = word
        curr.count = time

    def __lt__(self, other):  # 这里是给TrieNode可比较的特性，不然的话排序的时候要另外加东西辅助
        if self.count < other.count:
            return True
        elif self.count > other.count:
            return False
        return self.word > other.word

    def get_words(self):  # 搜索从当前节点往下的所有单词，不一定是叶子节点
        ans, queue = list(), deque([self, ])
        while queue:  # 深搜广搜都行，我用了广搜
            curr = queue.popleft()
            if curr.count:  # 只有当前的count不为0，才代表一个单词
                heapq.heappush(ans, curr)  # 用一个大小为3的堆来筛选最终频率高、字典序小的单词
                if len(ans) > 3: heapq.heappop(ans)  # 维护堆的大小

            for node in curr.next.values():
                queue.append(node)

        ans.sort(reverse = True)  # 把堆排个序就是答案了，注意要逆序
        return [node.word for node in ans]


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()  # Trie的根节点
        self.curr = self.root  # 当前遍历到的节点
        self.word = ""  # 当前查询的句子
        # 初始化Trie
        for word, time in zip(sentences, times):
            self.root.insert(word, time)

    def input(self, c: str) -> List[str]:  # 三种情况：1. 结束 2. 没这个前缀 3. 有这个前缀
        if c == '#':
            return self.process_end(c)
        if c not in self.curr.next:
            return self.process_not_in(c)
        return self.process_in(c)

    def process_end(self, c):  # 结束
        self.curr.word = self.word  # 把到目前为止的查询记录插到Trie里去
        self.curr.count += 1
        self.curr = self.root  # 初始化当前查询的节点和单词，curr and word
        self.word = ""
        return list()

    def process_not_in(self, c):  # 没有找到这个前缀
        self.curr = self.curr.next[c]  # 创建新的节点，defaultdict不用额外初始化
        self.word += c  # 维护当前的查询记录
        return list()

    def process_in(self, c):  # 有这个前缀
        self.curr = self.curr.next[c]  # 走到具有这个前缀的下一个节点
        self.word += c  # 维护当前的查询记录

        return self.curr.get_words()  # 按频率和字典序返回结果


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
