# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/3 9:06'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    A, B = map(int, input().split())
    ans = (A + B) * (B - A + 1) / 2
    cur = 0
    for i in range(A, B + 1):
        if cur == 4:
            print(f"{i:>5}")
        else:
            print(f"{i:>5}", end = "")
            if i == B:
                print()
        cur = (cur + 1) % 5
    print(f"Sum = {int(ans)}")

    end = time.perf_counter()
    print(end - start)
