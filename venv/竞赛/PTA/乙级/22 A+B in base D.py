# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/15 10:55'

import time

if __name__ == '__main__':
    start = time.perf_counter()


    def ten_to_k(n, x):  # 10进制转36以内进制
        a = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)]
        b = []
        while n > 0:
            y = n % x
            b.append(a[y])
            n = n // x
        b.reverse()
        return b


    a, b, d = map(int, input().split())

    c = a + b
    if c == 0:
        print(0)
    else:
        print("".join(ten_to_k(c, d)))

    end = time.perf_counter()
    print(end - start)
