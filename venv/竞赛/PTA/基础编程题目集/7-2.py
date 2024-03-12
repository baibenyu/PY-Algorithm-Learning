# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/2 10:44'


import time

if __name__ == '__main__':
    start = time.perf_counter()

    time, pas = map(int, input().split())
    hour = time // 100
    minute = (time % 100 + pas) % 60
    hour += (time % 100 + pas) // 60
    print(f'{hour}{minute:02}')

    end = time.perf_counter()
    print(end - start)