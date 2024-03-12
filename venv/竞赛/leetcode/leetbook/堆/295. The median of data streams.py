# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/20 15:46'
import heapq
import time


class MedianFinder:
    # 通过维护大小根堆的长度接近对半分,来让中位数处于堆顶
    def __init__(self):
        self.queMin = list()  # 大根堆,存储可能是中位数的小于的数
        self.queMax = list()  # 小根堆,存储可能是中位数的大于的数

    def addNum(self, num: int) -> None:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if not queMin_ or num <= -queMin_[0]:  # 当大根堆为空或数字小于当前中位数
            heapq.heappush(queMin_, -num)  # 用-号实现大根堆
            if len(queMax_) + 1 < len(queMin_):  # 如果小根堆的长度+1小于大根堆长度,说明两边长度不平衡,应该让大根堆把栈顶移到小根堆,维持一边大于,一边小于
                heapq.heappush(queMax_, -heapq.heappop(queMin_))
        else:
            heapq.heappush(queMax_, num)
            if len(queMax_) > len(queMin_):
                heapq.heappush(queMin_, -heapq.heappop(queMax_))

    def findMedian(self) -> float:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if len(queMin_) > len(queMax_):
            return -queMin_[0]
        return (-queMin_[0] + queMax_[0]) / 2


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
