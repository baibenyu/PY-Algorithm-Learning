# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/14 11:43'

import time

n = int(input().strip())

ans = []
start = time.clock()
for i in range(n, 0, -1):
    count = 0
    temp = i
    if temp not in ans:
        while count < 2:
            if temp == 1:
                count += 1
            if temp not in ans:
                ans.append(temp)
                if temp & 1:
                    temp = temp * 3 + 1
                else:
                    temp = temp >> 1
            else:
                break
    else:
        continue
print(max(ans))
end = time.clock()
print(end - start)