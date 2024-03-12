# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/2 10:01'


import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input()) / 100
    inch = n / 0.3048
    foot = int(n / 0.3048)
    inch = int((inch - foot) * 12)
    print(f'{foot} {inch}')

    end = time.perf_counter()
    print(end - start)