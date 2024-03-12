# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/4 9:14'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    a, b = map(int, input().split('/'))
    ta, tb = a, b
    if a == b:
        print(f"1/1")
    else:
        while tb != 0:  # 辗转相除求最大公约数
            tb, ta = ta % tb, tb
        print(f"{a // ta}/{b // ta}")

    end = time.perf_counter()
    print(end - start)
