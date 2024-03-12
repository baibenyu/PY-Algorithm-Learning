# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/29 10:42'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import math


    def isprime(n):
        if n > 1:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        else:
            return False


    n = int(input())
    for i in range(n):
        k, m = map(int, input().split())
        print(f"Case {i + 1}")
        flag = 0
        if 9 * k <= m:
            print("No Solution")
        else:
            for j in range(10 ** (k - 1), 10 ** k):
                curj = 0
                tempj = j
                while tempj:
                    curj += tempj % 10
                    tempj //= 10

                if curj != m:
                    continue
                else:
                    cura = 0
                    tempa = j + 1
                    while tempa:
                        cura += tempa % 10
                        tempa //= 10
                    common = math.gcd(curj, cura)
                    if common > 2 and isprime(common):
                        print(cura, j)
                        flag = 1
            if not flag:
                print("No Solution")

    end = time.perf_counter()
    print(end - start)
