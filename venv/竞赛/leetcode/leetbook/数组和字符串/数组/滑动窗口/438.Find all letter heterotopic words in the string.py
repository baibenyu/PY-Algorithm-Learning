# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/2 16:05'
from typing import List


class Solution:
    # 方法一:哈希表+滑动窗口
    # 优化方向->将字母转用asill码表示
    def findAnagrams(self, s: str, p: str) -> List[int]:
        import collections
        length = len(p)
        index = []
        p_c = collections.Counter(p)
        s_c = collections.Counter(s[:length])
        for i in range(length, len(s)):
            if s_c == p_c:  # 之所以可以这样比较,是因为Counter自带defaultdict,碰到未存入的元素默认返回0
                index.append(i - length)
            s_c[s[i]] += 1  # 滑动窗口,左边界对应字母数-1,右边界对应字母数+1
            s_c[s[i - length]] -= 1
        if s_c == p_c:
            index.append(len(s) - length)
        return index

    # 方法二:滑动窗口--用数组记录出现次数
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1

            if s_count == p_count:
                ans.append(i + 1)

        return ans
