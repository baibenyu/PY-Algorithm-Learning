# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/28 21:11'

class Solution:
    # 方法一:暴力--遍历所有起始位置
    # 将所有字符的状态设为False,若为True说明出现过,跳出循环,从下一个起始位置继续遍历
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        set1 = set(s)
        if not s:
            return 0
        elif length == 1:
            return 1
        else:
            ans = []
            for i in range(length):
                dict1 = dict(zip(set1, [False] * len(set1)))
                count = 1
                dict1[s[i]] = True
                for j in range(i + 1, length):
                    if not dict1[s[j]]:
                        dict1[s[j]] = True
                        count += 1
                    else:
                        break
                ans.append(count)
            return max(ans)

    # 方法二:双指针--滑动窗口
    def lengthOfLongestSubstring2(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])  # 移除到无重复字符为止
            while rk + 1 < n and s[rk + 1] not in occ:  # 移动直到下一个字符是重复字符为止
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans
