# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/1 7:52'

import time
# 注意:不适用于负权图
# 步骤:1--建立一个包含起始点到所有点的最短距离,以及最短路径中的上一个顶点,的表格.初始化为正无穷,起始点初始化为0
#     2--选取表中距离最短的顶点,遍历所有边,更新到其它顶点的最短距离以及最短路径中的上一个顶点
#     3--重复2直至所有点均被遍历一遍
if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
