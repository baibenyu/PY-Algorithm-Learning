# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/7 14:51'
import heapq
import time


class Solution:
    # 方法一:最小堆
    # 只含2,3,5为质因数说明该数可以只由2,3,5构成,第n个丑数也就是第n小的丑数,刚好是堆的特性
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                nxt = curr * factor
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)

    # 方法二:DP+三指针
    # dp表示第n位丑数是什么
    # 看成有三个丑数序列,每个丑数序列都是由前一个丑数*对应因数得来,求第n个相当于按从小到大合并三个序列,当遇到相同元素需要指针都移动
    def nthUglyNumber2(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:  # 不能用else
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
