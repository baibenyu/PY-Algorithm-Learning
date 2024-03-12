# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/17 12:03'

import time

start = time.clock()

size = [int(i) for i in input().split()]
a, b, c = size[0], size[1], size[2]
re = []
a %= b

while c > 10:  # 缩减问题规模
    a = a * (10 ** 10) % b
    c -= 10

for i in range(c + 2):  # 模拟除法,一次输出得到的结果
    if i >= c - 1:
        re.append(str(int(10 * a / b)))
    a = a * 10 % b
print(''.join(re))

end = time.clock()
print(end - start)
