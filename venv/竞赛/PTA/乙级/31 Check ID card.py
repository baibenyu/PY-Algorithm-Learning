# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/17 15:49'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    flag = True
    dict1 = dict(zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]))
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    for i in range(n):
        ID = input()
        cur = 0
        if ID[:17].isdigit():
            for j in range(17):
                cur += weight[j] * int(ID[j])
            if dict1[cur % 11] != ID[17]:
                print(ID)
                flag = False
        else:
            print(ID)
            flag = False
    if flag:
        print("All passed")

    end = time.perf_counter()
    print(end - start)
