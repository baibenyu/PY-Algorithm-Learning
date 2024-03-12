# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/14 16:17'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    list1, list2, list3, list4 = [], [], [], []
    n, l, h = map(int, input().split())
    count = 0
    for i in range(n):
        ID, virtue, ability = map(int, input().split())
        if virtue >= l and ability >= l:
            if virtue >= h and ability >= h:
                list1.append((ID, virtue, ability))
            elif virtue >= h:
                list2.append((ID, virtue, ability))
            elif virtue >= ability:
                list3.append((ID, virtue, ability))
            else:
                list4.append((ID, virtue, ability))
            count += 1

    order = lambda x: (x[1] + x[2], x[1], -x[0])
    list1.sort(key = order, reverse = True)
    list2.sort(key = order, reverse = True)
    list3.sort(key = order, reverse = True)
    list4.sort(key = order, reverse = True)
    list1 = list1 + list2 + list3 + list4
    print(count)
    for each in list1:
        print(each[0], each[1], each[2])

    end = time.perf_counter()
    print(end - start)
