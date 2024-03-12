# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/23 7:19'

import time
from collections import defaultdict


class Solution:
    # 方法一:滑动窗口+哈希表--是一个定长窗口
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        n = len(S)
        if K > n:
            return 0

        char_cnt = defaultdict(int)
        kind = 0  # 滑动窗口内的字符种类
        for i in range(K):  # 第一个滑动窗口内的情况
            if S[i] not in char_cnt:
                kind += 1
            char_cnt[S[i]] += 1
        res = 1 if kind == K else 0

        for R in range(K, n):
            if char_cnt[S[R]] == 0:  # 进R
                kind += 1
            char_cnt[S[R]] += 1
            char_cnt[S[R - K]] -= 1  # 弹L
            if char_cnt[S[R - K]] == 0:
                kind -= 1

            if kind == K:  # 更新res
                res += 1
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
