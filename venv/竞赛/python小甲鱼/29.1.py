def compare(file_name1,file_name2):
    f1 = open(file_name1)
    f2 = open(file_name2)
    list1 = []
    list2 = []
    list3 = []
    for each_line in f1:
        list1.append(each_line)
    for each in f2:
        list2.append(each)
    num = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            continue
        else:
            list3.append(i+1)
            num += 1
    print('两个文件共有%s个不同' % num)
    for i in list3:
        print('第%s行不一样\n' % i)


file_name1 = input('请输入第一个需要比较的文件名:')
file_name2 = input('请输入另一个需要比较的文件名:')
compare(file_name1,file_name2)
