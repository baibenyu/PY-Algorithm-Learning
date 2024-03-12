# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/12 20:11'

import time
import math

start = time.clock()


# 重点在于理清关系和边界
def SUM(upper_left, lower_right):
    sum_up = 0
    for a in range(int(upper_left[0]) - 1, int(lower_right[0])):
        for b in range(int(upper_left[1]) - 1, int(lower_right[1])):
            if type(matrix[a][b]) != str:
                sum_up += matrix[a][b]
            else:
                cur = matrix[a][b][3:].replace("(", "").replace(")", "")
                upper_left, lower_right = cur.split(":")
                upper_left = upper_left.split(",")
                lower_right = lower_right.split(",")
                if matrix[a][b][:3] == "SUM":
                    sum_up += SUM(upper_left, lower_right)
                elif matrix[a][b][:3] == "AVG":
                    sum_up += AVG(upper_left, lower_right)
                else:
                    sum_up += STD(upper_left, lower_right)
    return sum_up


def AVG(upper_left, lower_right):
    avg = SUM(upper_left, lower_right) / (
            (int(lower_right[0]) - int(upper_left[0]) + 1) * (int(lower_right[1]) - int(upper_left[1]) + 1))
    return avg


def STD(upper_left, lower_right):
    avg = AVG(upper_left, lower_right)
    sum_up = 0
    for p in range(int(upper_left[0]) - 1, int(lower_right[0])):
        for q in range(int(upper_left[1]) - 1, int(lower_right[1])):
            if type(matrix[p][q]) != str:
                sum_up += (matrix[p][q] - avg) ** 2
            else:
                cur = matrix[p][q][3:].replace("(", "").replace(")", "")
                upper_left, lower_right = cur.split(":")
                upper_left = upper_left.split(",")
                lower_right = lower_right.split(",")
                if matrix[p][q][:3] == "SUM":
                    sum_up += (SUM(upper_left, lower_right) - avg) ** 2
                elif matrix[p][q][:3] == "AVG":
                    sum_up += (AVG(upper_left, lower_right) - avg) ** 2
                else:
                    sum_up += (STD(upper_left, lower_right) - avg) ** 2
    variance = sum_up / (
            (int(lower_right[0]) - int(upper_left[0]) + 1) * (int(lower_right[1]) - int(upper_left[1]) + 1))
    return math.sqrt(variance)


n, m = map(int, input().strip().split())
matrix = []

for i in range(n):
    temp = input().split()
    for j in range(len(temp)):
        if "0" <= temp[j][0] <= "9":
            temp[j] = int(temp[j])
    matrix.append(temp)

for x in range(n):
    for y in range(m):
        if type(matrix[x][y]) == str:
            cur = matrix[x][y][3:].replace("(", "").replace(")", "")
            upper_left, lower_right = cur.split(":")
            upper_left = upper_left.split(",")
            lower_right = lower_right.split(",")
            if matrix[x][y][:3] == "SUM":
                matrix[x][y] = SUM(upper_left, lower_right)
            elif matrix[x][y][:3] == "AVG":
                matrix[x][y] = AVG(upper_left, lower_right)
            else:
                matrix[x][y] = STD(upper_left, lower_right)
        print('{:.2f}'.format(matrix[x][y]), end = " ")
    print()

end = time.clock()
print(end - start)
