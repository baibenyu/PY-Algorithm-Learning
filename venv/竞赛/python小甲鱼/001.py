# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2021/12/24 9:52'
import time

start = time.time()
number = []
for a in range(1000):
    for b in range(10000):
        number.append(a*1000+b*10000)
end = time.time()
print(end-start)

start = time.time()
number = []
for a in range(1000):
    c = a*1000
    for b in range(10000):
        number.append(c+b*10000)
end = time.time()
print(end-start)
