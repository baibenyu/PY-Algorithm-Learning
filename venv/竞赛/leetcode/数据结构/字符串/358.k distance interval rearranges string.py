# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/1 14:54'
import collections
import heapq
import time
from collections import Counter


class Solution:
    # 方法一:构造桶
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        c = Counter(s)
        chars = sorted(c.items(), key = lambda x: x[1], reverse = True)
        N = len(s)
        result = [None] * N
        i = 0
        j = k - 1
        curr = 0
        less_size = N // k
        more_size = less_size + 1
        more_track = N % k
        less_track = k - more_track
        for c, v in chars:
            if v > more_size:
                return ""
            elif v == more_size:
                if not more_track:
                    return ""
                # Use full track
                result[i::k] = [c] * v
                i += 1
                more_track -= 1
                curr = i
            elif v == less_size and less_track:
                # Use full track
                result[j::k] = [c] * v
                j -= 1
                less_track -= 1
            else:
                # Fill in order
                for _ in range(v):
                    result[curr] = c
                    curr += k
                    if curr >= N:
                        i += 1
                        curr = i
        return "".join(result)

    # 方法二:模拟--贪心+队列+堆
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s

        chr_freq = collections.Counter(s)

        maxHeap = [(-1 * freq, chr) for chr, freq in chr_freq.items()]
        heapq.heapify(maxHeap)

        Q = collections.deque()
        res = ""
        while maxHeap:
            freq, c = heapq.heappop(maxHeap)  # 要想实现，必须先弹出最大次数的那个
            freq *= -1

            res += c
            Q.append((freq - 1, c))

            if len(Q) == k:  # 能够构成一个长度为k的窗口。则后移
                f, c = Q.popleft()
                if f > 0:
                    heapq.heappush(maxHeap, (-1 * f, c))

        return res if len(res) == len(s) else ""


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
