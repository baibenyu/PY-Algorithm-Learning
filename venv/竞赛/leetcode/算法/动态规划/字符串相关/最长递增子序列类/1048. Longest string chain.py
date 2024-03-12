# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/22 9:32'

import time


class Solution:
    # 方法一:排序+字典dp
    def longestStrChain(self, words):
        words.sort(key = len)
        note = {}
        maxChain = 1
        for word in words:
            if word not in note:
                note[word] = 1
            for i in range(0, len(word)):  # 遇到每一个单词都检测有无前身,取前身最大
                newWord = word[:i] + word[i + 1:]
                if newWord in note:
                    note[word] = max(note[word], note[newWord] + 1)
            maxChain = max(maxChain, note[word])
        return maxChain


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
