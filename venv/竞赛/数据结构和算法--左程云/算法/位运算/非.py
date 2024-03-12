# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/9 21:05'

import time

if __name__ == '__main__':
    start = time.perf_counter()
    """
    1.不通过比较来判断两个数的大小a和b
    解:通过逻辑上加号和非组合不能同时成立的特点来判断
    """
    end = time.perf_counter()
    print(end - start)
