# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/23 8:52'

from typing import List


class Solution:
    # 方法一:对字母异位词进行排序,因为构成单词的字母完全相同,只是位置不同,进行排序后变成了相同的字符串
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
        mp = collections.defaultdict(list)  # 创建键值对会默认返回空列表

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())

    # 方法二:字母异位词的字母数量都完全相等,所以统计各字母出现次数,并以此为键来创建哈希表
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        import collections
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)

        return list(mp.values())
