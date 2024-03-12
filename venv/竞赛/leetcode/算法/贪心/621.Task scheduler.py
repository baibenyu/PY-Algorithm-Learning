# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/20 16:15'

from collections import Counter
from typing import List


class Solution:
    # 方法一:桶排序--设置大小为n+1的桶的个数为出现次数最多的那个元素的个数,桶的大小为N+1所以每 个桶都只能装不同的任务,最后一个桶不需要等待
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = Counter(tasks)  # Counter类会自动将可迭代序列根据元素计数
        nbucket = ct.most_common(1)[0][1]  # 取出最多的出现次数
        last_bucket_size = list(ct.values()).count(nbucket)  # 能出现在最后一个桶中的只有个数最多的元素,所以只需要统计有几个这样的元素即可
        res = (nbucket - 1) * (n + 1) + last_bucket_size  # 运行时间
        return max(res, len(tasks))  # 当任务重复率极低时,桶总是能够被充满,也即没有浪费任何时间,此时运行时间等于任务个数


