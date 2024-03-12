# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/15 20:37'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import re

    # 使用re的split同时按多个关键字符进行分割
    a, b, c = re.split('[.E]', input())

    # 负数以-开头，正数开头无符号
    if a[0] == '+':
        symbol = ''
    else:
        symbol = '-'

    a = a[1]
    # 如果指数为0，那直接输出
    if int(c) == 0:
        print(symbol + a + '.' + b)
    else:
        # 底数小数点后位数
        index = int(c[1:])

        if c[0] == '+':
            # 指数为正，则分两种情况
            if index >= len(b):
                print(symbol + a + b + '0' * (index - len(b)))
            else:
                print(symbol + a + b[0:index] + '.' + b[index:])
        else:
            print(symbol + '0.' + '0' * (index - 1) + a + b)

    end = time.perf_counter()
    print(end - start)
