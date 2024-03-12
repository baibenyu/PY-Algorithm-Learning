# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/14 8:46'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())

    for i in range(n):
        a, b, c = map(int, input().split())

        if a + b > c:
            print(f"Case #{i + 1}: true")
        else:
            print(f"Case #{i + 1}: false")

    end = time.perf_counter()
    print(end - start)
