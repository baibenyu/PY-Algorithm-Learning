# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/24 15:07'

import time


class Solution:
    # 方法一:字典序
    def nextGreaterElement(self, n: int) -> int:
        string = []
        cur = n
        while cur:
            string.append(str(cur % 10))
            cur = cur // 10
        string.reverse()
        length = len(string)

        i = length - 2  # 至少两个元素才能交换,排序
        while i >= 0 and string[i] >= string[i + 1]:  # 从后往前找到第一个小于后面元素的a[i]
            i -= 1

        if i >= 0:  # 若整个数组为降序,则在a[i]之后不存在比a[i]大的元素,不用执行while
            j = length - 1
            while j >= i and string[j] <= string[i]:  # 从后往前找到第一个大于a[i]的元素
                j -= 1
            string[i], string[j] = string[j], string[i]

        left, right = i + 1, length - 1
        while left < right:  # 因为原来顺序是降序,将i后的升序排序只需要逆转即可
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1

        ans = int("".join(string))
        if ans <= n or ans > 2 ** 31 - 1:
            return -1
        else:
            return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
