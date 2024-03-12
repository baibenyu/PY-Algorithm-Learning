# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/8 14:22'


n = int(input().strip())
list1 = []
list2 = []
for i in range(n):
    list1.append(input())
for i in range(n):
    print(list1[i])
    print()
while True:
    line = input().strip().split()
    if line == "":
        break
    else:
        for each in line:
            print(each)
            print()
