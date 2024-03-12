# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/20 21:21'

import time

start = time.clock()

s = list(input())
le = len(s)
m = s[:]
sl = ['ABT', 'ATB', 'BAT', 'BTA', 'TAB', 'TBA']
ans = []
for i in range(6):
    c = 0
    s = m
    a, b, t = sl[i][0], sl[i][1], sl[i][2]
    an, bn = s.count(a), s.count(b)
    ab, at = s[0:an].count(b), s[0:an].count(t)
    ba, bt = s[an:an + bn].count(a), s[an:an + bn].count(t)
    c = ab + at + bt + ba - min(ba, ab)
    ans.append(c)
print(min(ans))

end = time.clock()
print(end - start)
