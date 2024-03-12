# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/29 11:37'

import time

if __name__ == '__main__':
    start = time.perf_counter()


    def linklength(address):  # 求链表长度
        count = 0
        while address != "-1":
            address = linklist[address][1]
            count += 1
        return count


    p1, p2, n = input().split()
    n = int(n)
    linklist = dict()  # 建立链表
    for i in range(n):
        address, data, nextv = input().split()
        linklist[address] = [data, nextv]

    p1_len, p2_len = linklength(p1), linklength(p2)
    if p1_len < p2_len:  # 确保p1指向长链表的头部,p2指向短链表的头部
        p1, p2 = p2, p1

    prev = p2
    cur = linklist[p2][1]
    linklist[p2][1] = "-1"
    while cur != "-1":  # 反转链表
        temp = linklist[cur][1]
        linklist[cur][1] = prev
        prev = cur
        cur = temp

    p2 = prev
    ans = []
    for i in range(n):
        if (i + 1) % 3 == 0 and p2 != "-1":
            ans.append([p2, linklist[p2][0], linklist[p2][1]])
            p2 = linklist[p2][1]
        else:
            ans.append([p1, linklist[p1][0], linklist[p1][1]])
            p1 = linklist[p1][1]

    for i in range(n - 1):
        print(ans[i][0], ans[i][1], ans[i + 1][0])
    print(ans[-1][0], ans[-1][1], "-1")

    end = time.perf_counter()
    print(end - start)
