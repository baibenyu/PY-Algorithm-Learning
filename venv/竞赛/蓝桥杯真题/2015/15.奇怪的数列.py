# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/12 20:26'

import time

start = time.clock()

string = list(input().strip())
n = int(input().strip())

for i in range(n):
    temp = ""
    cur = 0
    length = len(string)
    while cur < length:
        cur_str = string[cur]
        count = 1
        while cur < length - 1 and string[cur] == string[cur + 1]:  # 滑动窗口
            cur += 1
            count += 1
        temp = temp + str(count) + cur_str
        cur += 1
    string = temp

print(string)

end = time.clock()
print(end - start)
