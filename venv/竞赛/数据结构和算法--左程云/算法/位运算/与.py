# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/9 21:05'

import time

if __name__ == '__main__':
    """
    性质:
    1.a&(-a) = 最低位的1
    2.a&(a-1) = 去掉最低位的1后,剩下的高位
    3.a&b = c 时,c向左移动一位,就是a和b相加的进位信息,因为与运算,当且仅当a和b二进制位同时为1才得1
    i = a^b , j = (a&b)<<1
    推导可得: a+b = i + j ,注意!!!可能有多重进位,所以必须执行该运算直至j等于0,即进位等于0时才是最终结果!!!
    
    """
    start = time.perf_counter()
    """
    1.一个数是否是2的整数次幂
    解:利用性质2,直接判断是否等于0即可
    2.一个数是否是4的整数次幂
    解:转化问题->只有1个1,且1位于二进制下的偶数位->与一个32位二进制位时,所有偶数位上都为1的数,看是否等于1,是1则是
    """
    end = time.perf_counter()
    print(end - start)
