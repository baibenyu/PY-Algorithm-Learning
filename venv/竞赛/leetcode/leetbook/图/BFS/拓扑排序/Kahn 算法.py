# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/2 8:25'

import time
# 经典适用于前置以及后续的结点关系
# 步骤:1--存储所有入度为0的点,并将入度为0的点入队
#     2--弹出队头元素,遍历它的所有后续结点,将后续结点的入度减一,即已学习当前结点.若后续结点入度减到0,入队.
#     3--重复2直至队列为空
if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
