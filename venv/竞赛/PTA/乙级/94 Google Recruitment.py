# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/26 21:31'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import math


    def isPrime(n):
        if n <= 3:
            return n >= 2
        else:
            if (n + 1) % 6 != 0 and (n - 1) % 6 != 0:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
        return True


    s, n = map(int, input().split())  # 获取两个数字：s是题目要求，不做他用，n是切割长度
    m = input()  # 输入的字符串（数字）
    if n <= len(m):  # 如果n>m的长度，就没有判断的必要了，可以直接跳过
        for i in range(len(m) - n + 1):  # 然后一个个遍历判断
            if isPrime(int(m[i:i + n])):  # 找到符合要求的字符串以后，输出然后退出程序
                print(m[i:i + n])
                exit(0)
    print('404')

    end = time.perf_counter()
    print(end - start)
