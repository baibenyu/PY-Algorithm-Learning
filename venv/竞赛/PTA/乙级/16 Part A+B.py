# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/14 16:17'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    a, da, b, db = input().split()
    ac, bc = a.count(da), b.count(db)
    if ac != 0 and bc != 0:
        print(int(ac * da) + int(bc * db))
    elif ac != 0:
        print(int(ac * da))
    elif bc != 0:
        print(int(bc * db))
    else:
        print(0)

    end = time.perf_counter()
    print(end - start)
