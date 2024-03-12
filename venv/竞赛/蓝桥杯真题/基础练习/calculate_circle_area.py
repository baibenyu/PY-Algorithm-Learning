# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/29 9:53'

import math

while True:
    try:
        r = int(input())
        area = r ** 2 * math.pi
        print("{:.7f}".format(area))
    except:
        break
