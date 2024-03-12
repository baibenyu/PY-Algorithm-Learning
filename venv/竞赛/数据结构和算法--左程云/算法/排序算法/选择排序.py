# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/2 15:36'

import time


def selectsort(arr): # 实现方式:依次选取最小值进行升序排列
    n = len(arr)
    for i in range(n):
        minindex = i
        for j in range(i+1,n):
            minindex = j if arr[j] < arr[minindex]
        swap(arr,i,minindex)

def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]

if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
