# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/3 22:15'

class Solution:
    # 方法一:暴力,遍历所有子串并判断是否是回文子串
    def countSubstrings(self, s: str) -> int:
        def check(string: str):
            length = len(string)
            for i in range(length // 2):
                if string[i] != string[length - i - 1]:
                    return False
            return True

        s_len = len(s)
        count = s_len
        for x in range(2, s_len + 1):
            for y in range(s_len - x + 1):
                if check(s[y:y + x]):
                    count += 1

        return count

    # 方法二:动态规划
    # dp表示i到j范围内的子串是否是回文串,由遍历顺序:左下->右上
    def countSubstrings2(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s) - 1, -1, -1):  # 注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    result += 1
                    dp[i][j] = True
        return result

    # 方法三:中心扩展法
    def countSubstrings3(self, s: str) -> int:
        ans = 0
        length = len(s)
        for i in range(length):  # 回文子串长度是奇数的情况
            left = right = i
            while left >= 0 and right < length and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        for j in range(length - 1):  # 回文子串长度是偶数的情况
            left, right = j, j + 1
            while left >= 0 and right < length and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

    # 方法四:manacher算法
    # 因为每个中心对应的回文串的数量都是回文半径//2,因此在算法过程中将最大半径改为记录每个中心对应的回文串数量
    def countSubstrings4(self, s: str) -> int:

        def manacherstring(string: str):
            s1 = "#"
            for x in range(len(string)):
                s1 += string[x]
                s1 += "#"
            return s1

        if not s or len(s) == 0:
            return 0
        else:
            string = manacherstring(s)
            length = len(string)
            r_array = [0 for _ in range(length)]
            center, rlimit = -1, -1
            ans = 0
            for i in range(length):
                if rlimit > i:
                    r_array[i] = min(r_array[2 * center - i], rlimit - i)
                else:
                    r_array[i] = 1
                while i + r_array[i] < length and i - r_array[i] > -1:
                    if string[i + r_array[i]] == string[i - r_array[i]]:
                        r_array[i] += 1
                    else:
                        break
                if i + r_array[i] > rlimit:
                    rlimit = i + r_array[i]
                    center = i
                ans += r_array[i] // 2
            return ans