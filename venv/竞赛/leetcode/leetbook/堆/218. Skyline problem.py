# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/1 15:18'
import heapq
import time
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        # 共有两类关键点出现的位置：
        # 1、垂直线向上走转水平线的位置，位置为：出现更高高度的地方
        # 2、垂直线向下走转水平线的位置，位置为：当前最大高度和第二高度相交的地方

        ans, stack = [], []
        heapq.heapify(stack)  # 用最小堆来存放右端点和高度,方便每次弹出的是小的右端点
        # 如果堆里面有元素[右端点,高度]，那么此时可能关键点只能在垂直线向下走转水平线的位置，即第2类关键点

        cur_max_height = 0  # 初始化当前最大高度

        for left, right, height in buildings:
            # 先判断第2类关键点
            while stack and stack[0][0] < left:  # 堆底元素也小于当前左端点，即堆内所有元素都小于当前左端点
                # 注意点：首先第1类关键点先出现，第2类关键点后出现，再第1类关键点。。。。因为题目要求关键点按x坐标升序输出，所以当堆内所有元素都小于当前左端点，就不能先判断第1类关键点了，要先判断第2类关键点。
                # 判断堆内的右端点是否有第2类关键点出现，判断方法：弹出元素与当前最大高度比较（第2类关键点的定义）
                cur_right, cur_height = heapq.heappop(stack)
                if cur_height == cur_max_height:  # 如果当前弹出的高度是当前最大高度
                    # 那么第二高度是堆内的高度最高的高度（特别的，如果堆内没有元素了，为0）
                    second_height = max(stack, key = lambda x: x[1])[1] if stack else 0
                    if second_height != cur_max_height:  # 当然这两者不能相等
                        cur_max_height = second_height  # 更新当前最大高度
                        ans.append([cur_right, cur_max_height])
            # 再判断第1类关键点
            if height > cur_max_height:  # 判断左端点是否有第1类关键点出现
                cur_max_height = height  # 更新当前最大高度
                # 下面这个避免左端点重复的问题，因为左端点非严格递增
                if ans and left == ans[-1][0]:
                    ans[-1][1] = cur_max_height
                else:
                    ans.append([left, cur_max_height])
            # 每次循环把右端点和高度入堆
            heapq.heappush(stack, [right, height])

        # 当一次遍历完，堆内仍然可能有元素，需要二次判断第2类关键点，判断方法同上
        while stack:
            cur_right, cur_height = heapq.heappop(stack)
            if cur_height == cur_max_height:  # 如果当前弹出的高度是当前最大高度
                # 那么第二高度是堆内的高度最高的高度（特别的，如果堆内没有元素了，为0）
                second_height = max(stack, key = lambda x: x[1])[1] if stack else 0
                if second_height != cur_max_height:  # 当然这两者不能相等
                    cur_max_height = second_height  # 更新当前最大高度
                    ans.append([cur_right, cur_max_height])

        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
