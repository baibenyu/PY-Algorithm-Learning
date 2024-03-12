# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/13 8:41'

import time
from typing import List


class Solution:
    # 方法一:哈希表--将字符串间的偏移量作为键值
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        import collections
        ans = collections.defaultdict(list)
        for each in strings:
            temp = [0]
            for i in range(1, len(each)):
                cur = ord(each[i]) - ord(each[i - 1])
                if cur < 0:  # 处理循环,偏移量均为正值
                    cur += 26
                temp.append(cur)
            ans[tuple(temp)].append(each)
        return list(ans.values())


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
