# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/3 8:51'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    Open, High, Low, Close = map(float, input().split())

    if Close < Open:
        print(f"BW-Solid", end = "")
    elif Close > Open:
        print(f"R-Hollow", end = "")
    else:
        print(f"R-Cross", end = "")

    if Low < Open and Low < Close:
        print(f" with Lower Shadow", end = "")
        if High > Open and High > Close:
            print(f" and Upper Shadow", end = "")
    elif High > Open and High > Close:
        print(f" with Upper Shadow", end = "")
    print()

    end = time.perf_counter()
    print(end - start)
