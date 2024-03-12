# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/4 20:02'
import collections
import heapq
import time


class Solution:
    # 方法一:Counter类
    def frequencySort(self, s: str) -> str:
        return ''.join([i * j for i, j in collections.Counter(s).most_common()])  # 方法自带按次数降序遍历

    # 方法二:哈希表统计+排序重排
    def frequencySort2(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        items = [(-val, key) for key, val in count.items()]
        res = ""
        for val, key in sorted(items):
            res += key * (-val)
        return res

    # 方法三:大根堆,依次弹出栈顶
    def frequencySort3(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        items = [(-val, key) for key, val in count.items()]
        heapq.heapify(items)
        res = ""
        while items:
            val, key = heapq.heappop()
            res += key * (-val)
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
