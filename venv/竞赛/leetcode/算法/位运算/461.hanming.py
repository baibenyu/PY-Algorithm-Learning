# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/9 9:22'

def hammingDistance_1(x: int, y: int) -> int:  # 除二取余法,本质上就是将十进制转为二进制,逐位比较是否相同
    count = 0
    while x > 0 or y > 0:
        if x % 2 != y % 2:
            count += 1
        x = x // 2
        y = y // 2
    print(count)
    return count


def hammingDistance_2(x: int, y: int) -> int:  # 二进制,位置上数字不同->位运算中的异或运算
    xor = x ^ y
    count = 0
    while xor > 0:
        count += 1
        xor &= xor - 1  # 一个数&本身减一可以将二进制下最右边的1变为0,其它不变
    return count


def hammingDistance_3(x: int, y: int) -> int:  # 思路同上,但借助Python函数bin()将异或结果转为字符串,然后统计出现了几个1,即有几处不同
    return bin(x ^ y).count("1")
