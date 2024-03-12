# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/26 20:51'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import collections

    dict1 = collections.defaultdict(list)
    n, m = map(int, input().split())
    for i in range(n):
        a, b = input().split()
        dict1[a].append(b)
        dict1[b].append(a)
    for j in range(m):
        nums = input().split()
        flag = False
        for each in nums[1:]:
            if not flag:
                for value in dict1[each]:
                    if value in nums[1:]:
                        print("No")
                        flag = True
                        break
            else:
                break
        if not flag:
            print("Yes")

    end = time.perf_counter()
    print(end - start)
