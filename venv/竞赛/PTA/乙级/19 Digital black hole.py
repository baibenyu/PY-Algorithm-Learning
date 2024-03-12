# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/15 9:22'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    # 输入数字，若不足4位，则使用rjust在左侧用0补全至4位
    n = list(input().rjust(4, "0"))
    result = -1

    while result != 0 and result != 6174:
        n.sort(reverse = True)
        a = "".join(n)
        n.sort()
        b = "".join(n)
        result = int(a) - int(b)
        print(f"{a:04} - {b:04} = {result:04}")
        n = list(f"{result:04}")

    end = time.perf_counter()
    print(end - start)
