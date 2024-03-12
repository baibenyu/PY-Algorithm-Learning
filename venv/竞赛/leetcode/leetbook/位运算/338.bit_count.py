# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/10 9:02'

class Solution:
    # 方法一:将整数转为二进制字符串,并数1的个数
    def countBits_1(self, n: int) -> []:
        ans = []
        for i in range(n + 1):
            ans.append(bin(i).count("1"))
        return ans

    # 方法二:Brian Kernighan算法--利用(一个数)&(本身-1)会将最右边的1变为0的性质,来数有几个1
    def countBits_2(self, n: int) -> []:
        ans = [0]
        for i in range(1, n + 1):
            count = 0
            while i > 0:
                count += 1
                i &= i - 1
            ans.append(count)
        return ans

    # 方法三:动态规划(1)--最高有效位--即每一个整数的二进制表示下1的个数都等于减掉最高有效位后的二进制表示下1的个数+1
    def countBits_3(self, n: int) -> []:
        ans = [0]
        highbit = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                highbit = i
            ans.append(ans[i - highbit] + 1)
        return ans

    # 方法四:动态规划(2)--最低有效位--偶数2进制下右移一位(即整除以2),1的个数不变;奇数2进制下右移一位,1的个数减一
    def countBits_4(self, n: int) -> []:
        ans = [0]
        for i in range(1, n + 1):
            ans.append(ans[i >> 1] + i & 1)

        return ans

    # 方法五:动态规划(3)--最低设置位--根据Brian Kernighan算法的性质可知,每进行一次y=x&(x-1),二进制下y的1的个数会比x少一
    def countBits_5(self, n: int) -> []:
        ans = [0]
        for i in range(1, n + 1):
            ans.append(ans[i & (i - 1)] + 1)
        return ans
