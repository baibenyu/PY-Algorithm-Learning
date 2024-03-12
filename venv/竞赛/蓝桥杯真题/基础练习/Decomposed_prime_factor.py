# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/2 19:35'
import math

# while True:
# try:
a, b = map(int, input().strip().split())
list1 = []
for x in range(2, b + 1):
    flag = True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            flag = False
            break
    if flag:
        list1.append(x)

for y in range(a, b + 1):
    temp = y
    if temp in list1:
        print(str(y)+"="+str(y))
    else:
        print(str(y)+"=", end = "")
        for z in list1:
            while temp > 1:
                if temp % z == 0:
                    temp = temp // z
                    if temp > 1:
                        print(str(z)+"*", end = "")
                    else:
                        print(str(z))
                else:
                    break

# except BaseException as e:
#     print(e)
