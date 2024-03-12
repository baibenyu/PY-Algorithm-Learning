# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/12 14:32'

import time


class Solution:
    # 方法一:埃式筛--所有大于根号n的合数都能被小于根号n的素数表示
    def countPrimes(self, n: int) -> int:
        # 最小的质数是 2
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0  # 0和1不是质数，先排除掉

        # 埃式筛，把不大于根号 n 的所有质数的倍数剔除
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                # 从i**2开始,因为之前的数字都已经被筛选了一遍,步长i表示所有i的倍数都是合数,后面求有几个i的倍数应该赋值为0,即合数
                isPrime[i ** 2:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)

    # 方法二:欧几里得筛--线性筛
    def countPrimes2(self, n: int) -> int:
        if n < 2:
            return 0
        prime = [-1 for _ in range(n)]  # 存储当前找到的素数因子,从小到大排列
        pn = 0  # 标记当前找到的素数个数

        mark = [True for _ in range(n)]  # 标记数字是否是素数
        mark[0] = mark[1] = False

        for x in range(2, n):  # 对每一个数都进行了一次素数倍筛选
            if mark[x]:
                prime[pn] = x
                pn += 1
            pi = 0
            while pi < pn and x * prime[pi] < n:  # 可以理解成质因数分解的反过程
                mark[x * prime[pi]] = False  # 当前数的素数倍,保证合数仅被最小素数因子筛选出来,不重复筛选
                pi += 1

        return pn


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
