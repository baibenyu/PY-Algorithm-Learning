# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/4 13:58'

class Solution:
    # 方法一:manacher算法
    # 当前回文中心的回文半径总共分四种情况:1.完全在最大右边界外2.(1)完全在最大右边界内(2)部分在最大右边界内(3)刚好与最大右边界重合
    # 1和2.3情况都需要用中心扩展法暴力搜索,而2.1(小框架为什么不能再扩?)和2.2(大框架为什么不能再扩?)都基于对称性可将自身是否可扩的位置与之前对称位置是否可扩联系到一起,能直接得出结论
    def countSubstrings(self, s: str) -> int:

        def manacherstring(string: str):
            s1 = "#"
            for x in range(len(string)):
                s1 += string[x]
                s1 += "#"
            return s1

        if not s or len(s) == 0:
            return 0
        else:
            string = manacherstring(s)  # 将奇数和偶数字符串处理为奇数字符串
            length = len(string)
            r_array = [0 for _ in range(length)]  # 各中心点的回文半径
            center, rlimit = -1, -1  # 中心点及相应的右边界
            max_r = float("-inf")
            for i in range(length):
                if rlimit > i:
                    r_array[i] = min(r_array[2 * center - i], rlimit - i)  # 处理了2.1和2.2两种情况,都取较小的半径
                else:
                    r_array[i] = 1  # 半径至少为1,即本身
                while i + r_array[i] < length and i - r_array[i] > -1:  # 是否抵达整个字符串的左右边界
                    if string[i + r_array[i]] == string[i - r_array[i]]:
                        r_array[i] += 1
                    else:
                        break
                if i + r_array[i] > rlimit:  # 增长右边界
                    rlimit = i + r_array[i]
                    center = i
                max_r = max(max_r, r_array[i])
            return max_r - 1  # 拿到的回文半径是增长后的,原回文直径(长度)=增长后的半径-1=增长后的直径/2


s = Solution()
print(s.countSubstrings("ababa"))
