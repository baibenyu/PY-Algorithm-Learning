# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/16 10:02'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    # 要输入的人数
    n = int(input())
    # 用来存放符合要求的出生日期
    people = []

    # 依次进行输入
    for i in range(n):
        name, date = input().split(' ')
        # 符合要求的日期加入列表中
        if '1814/09/06' <= date <= '2014/09/06':
            people_info = [name]
            # 将日期按年、月、日拆分
            for j in date.split('/'):
                people_info.append(j)
            people.append(people_info)

    # 年、月、日作为三个关键字段进行升序排序
    # 生日日期最小的即为最年长者
    # 生日日期最大的即为最年幼者
    people = sorted(people, key = lambda x: (x[1], x[2], x[3]), reverse = False)
    # 如果没有年龄合格的人，就输出0
    if len(people) == 0:
        print(0)
    else:
        # 按要求输出
        print(str(len(people)) + ' ' + people[0][0] + ' ' + people[-1][0])

    end = time.perf_counter()
    print(end - start)
