# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/19 9:40'
import time
import collections
start = time.clock()

string = input().strip()
s = collections.Counter(string)
list1 = list(s.values())
list1.sort()
print(list1[-1]-list1[0])

end = time.clock()
print(end - start)