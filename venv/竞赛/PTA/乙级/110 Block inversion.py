# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/29 21:55'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    data = input().split()
    k = int(data[2])
    l = []
    l1 = [data[0]]
    l3 = []
    l4 = []
    l5 = []
    for i in range(int(data[1])):
        data1 = input().split()
        l.append(data1)
    while l1[-1] != '-1':
        for i in l:
            if i[0] == l1[-1]:
                l1.append(i[2])
                l3.append(i)

    for i in range(0, len(l3), k):
        l4.append(l3[i:i + k])
    l4.reverse()
    for i in l4:
        for j in i:
            l5.append(j)

    for i in range(len(l5) - 1):
        l5[i][-1] = l5[i + 1][0]
    l5[-1][-1] = '-1'
    for i in l5:
        print(" ".join(i))

    end = time.perf_counter()
    print(end - start)
