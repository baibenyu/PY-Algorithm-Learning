# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/6 22:09'

# 经典前缀树:每个结点记录两个值:1.有多少个字符串经过自己 2.有多少个字符串以自己为结尾
# 就是用树的路径来表示每个位置的字符
# 把字符串拆成单个字符,根据每个位置可能的字符创建孩子数组或者哈希表(路径)
# 那么拿到一个字符串只需根据头结点往下走,每一个节点的孩子可能性有26种(小写英文字母)
class Trie:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.pas = 0
        self.end = 0

    def insert(self, word: str) -> None:  # 插入单词建树
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node.children[ch].pas += 1
            node = node.children[ch]
        node.end += 1

    def countWordsEqualTo(self, word: str) -> int:  # 有几个word单词
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return 0
            else:
                node = node.children[ch]
        return node.end

    def countWordsStartingWith(self, prefix: str) -> int:  # 有几个以prefix为前缀的单词
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return 0
            else:
                node = node.children[ch]
        return node.pas

    def erase(self, word: str) -> None:  # 删除某个单词
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return
            else:
                node.children[ch].pas -= 1
                node = node.children[ch]
        node.end -= 1
