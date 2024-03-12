# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/13 15:45'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import re
    # 注意a==c
    n = input()
    for i in range(int(n)):
        s = input()
        if re.match(r'A*PA+TA*', s):  # 在字符串中进行匹配
            a = re.split(r'[P|T]', s)  # 以字符P,T进行分段
            if a[0] * len(a[1]) == a[2]:  # 条件判断
                print('YES')
            else:
                print('NO')
        else:
            print('NO')

    end = time.perf_counter()
    print(end - start)
