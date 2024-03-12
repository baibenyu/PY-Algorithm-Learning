# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/13 15:25'

import time

if __name__ == '__main__':

    t = int(input())
    for i in range(t):

        n = int(input())
        arr = list(map(int, input().split()))
        prefix = [0]
        minnum, maxnum = 0, 0
        for j in range(1, n + 1):
            prefix.append(prefix[j - 1] + arr[j - 1])
            if j == 1:
                minnum, maxnum = prefix[j], prefix[j]
            elif j < n:
                minnum, maxnum = min(minnum, prefix[j]), max(maxnum, prefix[j])
        ans1,ans2 = abs(prefix[n]*514-minnum*400),abs(prefix[n]*514-maxnum*400)
        if ans1 > ans2:
            print(ans1)
        else:
            print(ans2)
