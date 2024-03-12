# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/21 20:25'

import time
from typing import List


class Solution:
    # 方法一:哈希表--存储字母的起始位置和结束位置
    # 然后合并交叉的区间
    def partitionLabels(self, s: str) -> List[int]:
        interval = dict()
        for i in range(len(s)):
            if s[i] not in interval:
                interval[s[i]] = [i, i]
            else:
                interval[s[i]][1] = i
        list1 = list(interval.values())
        list1.sort(key = lambda x: x[0])
        ans = []
        left = list1[0][0]
        right = list1[0][1]
        for each in list1[1:]:
            if each[0] < right:
                if each[1] > right:
                    right = each[1]
            else:
                ans.append(right - left + 1)
                left = each[0]
                right = each[1]
        ans.append(right - left + 1)
        return ans

    # 方法二:贪心
    # 找到每个字母的最后出现位置,,然后重新遍历,每次都让end取到最大的end直至当前位置即为end,说明是一个区间
    def partitionLabels2(self, s: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i

        partition = list()
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition

