# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/20 8:19'
from typing import List


class Solution:
    # 方法一:如果存在一条从头到尾(从尾到头)的路线,换句话说就是这个路线中任意一个元素都能够到达其它的任意不处于该线路中元素,即不存在断点
    # 从后向前依次判断是否存在一个前方元素能够到达当前的最后位置,若存在则将这个元素设为可达的最后位置,继续循环向前判断,若能够将最后位置设为0,说明存在一条路线能够到达下标0
    # 如果不能,说明其中存在断点
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        final = length - 1
        while final > 0:
            flag = False
            for i in range(final - 1, -1, -1):
                if nums[i] >= final - i:  # 如果当前位置的跳数>=最后位置与当前位置的距离,说明可达
                    final = i
                    flag = True
                    break
            if not flag:  # 若遍历完后仍不可达
                return False
        return True

    # 方法二:贪心算法,实时更新一个最远可达的变量,若它大于最后一个元素的下标则存在这样一条路线
    def canJump2(self, nums: List[int]) -> bool:
        max_i = 0  # 初始化当前能到达最远的位置
        for i, jump in enumerate(nums):  # i为当前位置，jump是当前位置的跳数,enumerate函数是指同时遍历一个可迭代对象的索引和元素
            if i <= max_i < i + jump:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i + jump  # 更新最远能到达位置
        return max_i >= i
