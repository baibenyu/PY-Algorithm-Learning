# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/17 10:18'

import time

start = time.clock()


def ten_to_k(n, x):  # 10进制转36以内进制
    a = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)]
    b = []
    while n > 0:
        y = n % x
        b.append(a[y])
        n = n // x
    b.reverse()
    return b


def k_to_ten(string, x):  # 36以内进制转10进制
    target = 0
    length = len(string)
    for i in range(length):
        if "0" <= string[i] <= "9":
            target += (ord(string[i]) - 48) * (x ** (length - i - 1))
        else:
            target += (ord(string[i]) - 55) * (x ** (length - i - 1))
    return target


n = int(input().strip())
num = 0  # 只存储十进制表示
instruct = ""
pre_ins = ""  # 存储计算指令
k = 10
for i in range(n):
    instruct = input().strip().split()
    if instruct[0] == "CLEAR":
        num = 0
        pre_ins = ""
    elif instruct[0] == "NUM":
        if pre_ins != "":  # 至少有一个数字才能计算
            if pre_ins == "ADD":
                num += k_to_ten(instruct[1], k)
            elif pre_ins == "SUB":
                num -= k_to_ten(instruct[1], k)
            elif pre_ins == "MUL":
                num *= k_to_ten(instruct[1], k)
            elif pre_ins == "DIV":
                num //= k_to_ten(instruct[1], k)
            elif pre_ins == "MOD":
                num %= k_to_ten(instruct[1], k)
        else:
            num = k_to_ten(instruct[1], k)
    elif instruct[0] == "EQUAL":  # 转成目标进制再输出
        for each in ten_to_k(num, k):
            print(each, end = "")
        print()
    elif instruct[0] == "CHANGE":  # 记录当前进制
        k = int(instruct[1])
    else:
        pre_ins = instruct[0]
end = time.clock()
print(end - start)
