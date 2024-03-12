# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/14 19:59'

import time

start = time.clock()

n = int(input().strip())
ou = n & 0xaaaaaaaa  # 取二进制下的偶数位
ji = n & 0x55555555  # 取二进制下的奇数位
print((ou >> 1) ^ (ji << 1))

end = time.clock()
print(end - start)
