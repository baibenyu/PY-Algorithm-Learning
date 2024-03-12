# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/1 8:30'

while True:
    try:
        A = list(map(float, input().split())) # 难点在于理清思路,不要想一写一
        B = list(map(float, input().split()))

        Anew = [min(A[0], A[2]), min(A[1], A[3]), max(A[0], A[2]), max(A[1], A[3])]  # 重新定位坐标
        Bnew = [min(B[0], B[2]), min(B[1], B[3]), max(B[0], B[2]), max(B[1], B[3])]

        if (Anew[0] < Bnew[2] and Anew[1] < Bnew[3]) and (Bnew[0] < Anew[2] and Bnew[1] < Anew[3]):  # 判断是否相交
            x = Anew[::2] + Bnew[::2]
            y = Anew[1::2] + Bnew[1::2]
            x.sort()  # 对四个点的x坐标排序
            y.sort()  # 对四个点的y坐标排序

            xd = x[2] - x[1]  # 计算中间两个点的差值
            yd = y[2] - y[1]

            area = xd * yd
        else:
            area = 0
        print('%.2f' % area)
    except BaseException as e:
        print(e)
