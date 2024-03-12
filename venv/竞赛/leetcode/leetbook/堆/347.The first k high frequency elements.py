# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/23 9:38'
import collections
import heapq
from typing import List


class Solution:
    # 方法一:利用python自带的counter的方法求出
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        a = Counter(nums).most_common(k)
        b = [x[0] for x in a]
        return b

    # 方法二:前k个极值非常适合于堆结构,因为堆结构的根结点总是所有元素中的最值
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = [(val, key) for key, val in count.items()]  # 所以存储的时候,出现的次数在前
        return [item[1] for item in heapq.nlargest(k, heap)]  # 方法比较的是键值

    # 方法三:同样堆排序,通过限制堆的大小来让出现频率前k大的元素留在堆中,因为每次插入或替换元素,堆会自行维护自身的性质,即每次都留下出现频率前k个的元素在堆中
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = []
        for key, val in count.items():
            if len(heap) >= k:  # 堆满后,新的元素要与堆的根结点比较,若大于才能入堆
                if val > heap[0][0]:
                    heapq.heapreplace(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
        return [item[1] for item in heap]
