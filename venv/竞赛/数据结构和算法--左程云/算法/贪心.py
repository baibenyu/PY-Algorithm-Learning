# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/6 9:42'


import sys
import functools
import heapq


def combine():  # 字典序
    def custom_sort(x, y):
        if (x + y) < (y + x):
            return -1
        else:
            return 1

    n = int(input())
    strs = list()
    while n >= 0:
        l = sys.stdin.readline().strip()
        if l is not '':
            strs.append(l)
        n = n - 1
    strs = sorted(strs, key = functools.cmp_to_key(custom_sort))
    print(''.join(strs))


def lessMoneySplitGold(arr):  # 切金条问题

    q = list()
    heapq.heapify(q)
    for i in range(len(arr)):
        heapq.heappush(arr[i])
    ans = 0
    while len(q) > 1:
        cur = heapq.heappop(q) + heapq.heappop(q)
        ans += cur
        heapq.heappush(cur)
    return ans


def findmaximize(k, w, profits, captial):  # 创业问题
    sq, bq = list(), list()
    heapq.heapify(sq)
    heapq.heapify(bq)
    for i in range(len(profits)):
        heapq.heappush(sq, [captial[i], profits[i]])
    for j in range(k):
        while sq and sq[0][0] <= w:
            temp = heapq.heappop(sq)
            heapq.heappush(bq, [-temp[1], temp[0]])
        if not bq:
            return w
        w += heapq.heappop(bq)
    return w


if __name__ == '__main__':
    """
    1.会议室问题:要求特定时间段内进行最多次的会议,会议不能重叠
    解:贪心地根据结束时间排序,依次安排结束时间最早且不重叠的会议
    
    2.字典序:给定一个含多个字符串的数组,将字符串组合出的长字符串的最小字典序,必须用上每个字符串
    解:两个字符串组合后的字典序,根据字典序小的来组合排序,即排序的关键词是两个字符串组合后的字典序
    
    3.切金条问题:若干个人分一块金条,给定每个人分到的金条长度,求切金条的最小花费.
    切金条的花费--将一块金条切成任意大小不同的两块,都需要花费相当于金条长度的铜钱
    解:哈夫曼编码问题,最小生成树
    
    4.创业问题:给定初始资金和能做的项目数,再给定各项目的启动资金和相应利润,求做完项目后能获得的最大资金.
    解:大根堆+小根堆
    
    5.数据流的中位数
    解:第295题
    
    6.N皇后问题
    解:贪心+回溯,第51题
    """
