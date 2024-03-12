# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/31 8:59'

import time

# 步骤:1--将所有边按权值从小到大排序.并依次连接边对应的顶点
#     2--若连接后产生环则抛弃该边,进行下一条边的判断
#     3--直至所有顶点被连接,边的条数为n-1条
if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
