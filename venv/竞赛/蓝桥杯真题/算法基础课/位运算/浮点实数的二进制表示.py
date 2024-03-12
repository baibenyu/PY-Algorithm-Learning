# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/14 20:14'

import time

start = time.clock()
ans = "0."
n = float(input().strip())
# 小数采取乘2取整法
while n > 0:
    cur = n * 2
    if cur >= 1:
        ans += "1"  # 取整
        n = cur - 1  # 减去整数
    else:
        ans += "0"
        n = cur
    if len(ans) > 34:
        print("ERROR")
        break
print(ans)

end = time.clock()
print(end - start)
