# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/2 22:42'

class Solution:
    # 方法一:哈希表+滑动窗口
    # 先扩大窗口直至满足t的要求,再缩减无关元素直至碰到t中元素,记录最小长度,改变窗口起始位置再来一遍,直至遍历整个s字符串
    def minWindow(self, s: str, t: str) -> str:
        import collections
        need = collections.Counter(t)
        needCnt = len(t)
        left = 0
        res = (0, float('inf'))
        for right, string in enumerate(s):
            if need[string] > 0:
                needCnt -= 1
            need[string] -= 1
            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素

                while True:  # 步骤二：增加left，排除多余元素
                    string = s[left]
                    if need[string] == 0:  # 字典值为0说明是必须元素,即t中的元素,跳出循环
                        break
                    need[string] += 1  # 字典值负数表示多余
                    left += 1  # 缩减左边界

                if right - left < res[1] - res[0]:  # 记录结果
                    res = (left, right)
                need[s[left]] += 1  # 步骤三：left增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                left += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果
