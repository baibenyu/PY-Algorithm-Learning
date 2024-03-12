# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/20 10:02'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    from decimal import Decimal

    n = int(input())

    # 将浮点数都转换为Decimal类型，防止float计算结果不够精确的问题
    a = list(map(Decimal, input().split(' ')))

    result = Decimal(0)

    # a[i]在所有的片段中出现了(i+1)*(n-i)次
    for i in range(n):
        result = result + a[i] * (i + 1) * (n - i)

    # 使用quantize取小数点后两位并按格式输出
    print(result.quantize(Decimal('0.00')))

    end = time.perf_counter()
    print(end - start)
