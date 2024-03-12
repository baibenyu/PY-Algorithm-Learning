# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/21 14:20'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    N, K = map(int, input().split())
    stu = []
    for i in range(N):
        stu.append(input().split())
    stu = sorted(stu, key = lambda stu: stu[0])
    stu = sorted(stu, key = lambda stu: int(stu[1]), reverse = True)
    # print(stu)
    num = N // K
    final = N // K + N % K
    total = 0
    res = []
    for i in range(N):
        if total % 2 == 0:  # 偶数的话，就从右边开始追加
            res.append(stu[i][0])
        else:  # 奇数,从左边加
            res.insert(0, stu[i][0])
        total += 1
        if total == final:
            print(' '.join(res))
            final = num  # 除了最后一行外，其余各行人数相等
            res = []
            total = 0  # 清空

    end = time.perf_counter()
    print(end - start)
