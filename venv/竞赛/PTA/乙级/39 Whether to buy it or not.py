# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/18 15:56'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import collections

    h, red = input(), input()
    ch, cr = collections.Counter(h), collections.Counter(red)
    isok = True
    lack = 0
    for key in cr:
        if cr[key] > ch[key]:
            lack += cr[key] - ch[key]
            isok = False

    if isok:
        print("Yes", len(h) - len(red))
    else:
        print("No", lack)

    end = time.perf_counter()
    print(end - start)
