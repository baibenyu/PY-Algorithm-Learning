# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/25 9:33'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    p, m, n = map(int, input().split())
    dict1 = dict()
    for i in range(p):
        ID, score = input().split()
        dict1[ID] = [int(score), -1, -1]
    for i in range(m):
        ID, score = input().split()
        if ID not in dict1:
            dict1[ID] = [-1, int(score), -1]
        else:
            dict1[ID][1] = int(score)
    for i in range(n):
        ID, score = input().split()
        if ID not in dict1:
            dict1[ID] = [-1, -1, int(score)]
        else:
            dict1[ID][2] = int(score)
    ans = []
    for key, value in dict1.items():
        if value[0] >= 200:
            if value[1] > value[2]:
                G = int(value[1] * 0.4 + value[2] * 0.6 + 0.5)
            else:
                G = value[2]
            if G >= 60:
                ans.append((key, value[0], value[1], value[2], G))
    ans.sort(key = lambda x: x[0])
    ans.sort(key = lambda x: x[4], reverse = True)
    for each in ans:
        print(each[0], each[1], each[2], each[3], each[4])

    end = time.perf_counter()
    print(end - start)
