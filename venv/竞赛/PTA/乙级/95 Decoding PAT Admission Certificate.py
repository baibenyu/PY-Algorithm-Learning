# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/27 9:58'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n, m = map(int, input().split())
    dict1 = dict()
    list1 = list()
    for i in range(n):
        ID, score = input().split()
        dict1[ID] = int(score)
        list1.append((ID, int(score)))
    list1.sort(key = lambda x: x[0])
    list1.sort(key = lambda x: x[1], reverse = True)
    for j in range(m):
        command, require = input().split()
        print(f"Case {j + 1}: {command} {require}")
        if command == "1":
            flag = 0
            for x in range(len(list1)):
                if list1[x][0][0] == require:
                    print(list1[x][0], list1[x][1])
                    flag = 1
            if not flag:
                print("NA")
        elif command == "2":
            count, total = 0, 0
            for x in range(len(list1)):
                if list1[x][0][1:4] == require:
                    total += int(list1[x][1])
                    count += 1
            if count == 0 and total == 0:
                print("NA")
            else:
                print(count, total)
        else:
            places = [[_, 0] for _ in range(1000)]
            for x in range(len(list1)):
                if list1[x][0][4:10] == require:
                    places[int(list1[x][0][1:4])][1] += 1
            places.sort(key = lambda x: x[1], reverse = True)
            y = 0
            if places[y][1] == 0:
                print("NA")
            else:
                while places[y][1] != 0:
                    print(places[y][0], places[y][1])
                    y += 1

    end = time.perf_counter()
    print(end - start)
