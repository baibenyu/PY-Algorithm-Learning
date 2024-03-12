# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/24 7:52'

import time
from typing import List


class Solution:
    # 方法一:滑动窗口
    def totalFruit(self, fruits: List[int]) -> int:
        import collections
        picked = collections.Counter()
        left, right, ans = 0, 0, 0
        while right < len(fruits):
            picked[fruits[right]] += 1
            while len(picked) > 2:
                picked[fruits[left]] -= 1
                if picked[fruits[left]] == 0:
                    del picked[fruits[left]]
                left += 1
            right += 1
            ans = max(right - left, ans)
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
