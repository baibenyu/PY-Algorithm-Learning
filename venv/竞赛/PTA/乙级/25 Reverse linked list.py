# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/16 8:14'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    a = input().split()
    b = []
    for i in range(int(a[1])):
        b.append(input().split())

    # 在x列表中排序
    x = []
    for i in b:
        if i[0] == a[0]:
            x.append(i)
            break
    while x[-1][2] != '-1':
        for i in b:
            if i[0] == x[-1][2]:
                x.append(i)
                break
    s = []
    for i in range(0, int(a[1]), int(a[2])):
        if len(x[i:i + int(a[2])]) >= int(a[2]):
            temp = x[i:i + int(a[2])]
            temp.reverse()
            s = s + temp
        else:
            s = s + x[i:i + int(a[2])]
            break

    for i in range(len(s) - 1):
        s[i][2] = s[i + 1][0]
    s[-1][2] = '-1'

    for i in s:
        print(" ".join(i))

    end = time.perf_counter()
    print(end - start)
