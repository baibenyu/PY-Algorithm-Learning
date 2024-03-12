# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/5 13:12'

while True:
    #     try:
    length = int(input())
    list1 = list(input().strip())
    list2 = list1.copy()
    set1 = set(list2)
    count = 0
    odd = 0
    odd_num = ""
    for letter in set1:
        if list1.count(letter) % 2 == 1:
            odd += 1
            odd_num = letter
    if length % 2 == 1 and odd == 1 or length % 2 == 0 and odd == 0:

        for i in range((length - 1) // 2):  # 从两头向中间比较,碰到不同字母以左边为准
            if list1[i] != list1[length - 1 - i] and list1[i] != odd_num:  # 奇数个的字母会找不到,所以换右边为基准

                for q in range(length - 1 - i, i, -1):  # 从后往前找到最近的相同字母
                    if list1[i] == list1[q]:

                        for p in range(q, length - 1 - i):  # 冒泡排序交换过去
                            list1[p + 1], list1[p] = list1[p], list1[p + 1]
                            count += 1
                        break

                    else:
                        continue

            elif list1[i] != list1[length - 1 - i] and list1[i] == odd_num:

                for q in range(i, length - 1 - i):  # 从前往后找到最近的相同字母
                    if list1[length - 1 - i] == list1[q]:

                        for p in range(q, i, -1):  # 冒泡排序交换过去
                            list1[p - 1], list1[p] = list1[p], list1[p - 1]
                            count += 1
                        break

                    else:
                        continue
        print(count)
    else:
        print("Impossible")
# except BaseException as e:
#     print(e)
