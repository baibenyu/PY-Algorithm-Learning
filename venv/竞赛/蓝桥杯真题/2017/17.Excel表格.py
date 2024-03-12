# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/16 9:26'

import time

start = time.clock()


# 类进制转换,但起始位置为1不为0,26进制下,26等于26而不等于10,27等于11
def ten_to_twentysix(num):
    list1 = [chr(i) for i in range(65, 91)]
    res = []
    while num > 0:
        remainder = (num - 1) % 26
        num = (num - 1) // 26
        res.append(list1[remainder])
    res.reverse()
    return res


address = int(input().strip())
ans = "".join(ten_to_twentysix(address))
print(ans)

end = time.clock()
print(end - start)
