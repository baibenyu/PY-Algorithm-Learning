# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/13 10:24'

import time


class Solution:
    # 方法一:哈希表--求交集
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set(jewels)
        ans = 0
        for each in stones:
            if each in jewel:
                ans += 1
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
