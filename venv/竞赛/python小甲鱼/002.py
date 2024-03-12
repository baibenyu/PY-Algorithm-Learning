# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/16 9:03'


names = ("一", "二", "三", "si")
ages = (18, 19, 20)
jobs = ("老师", "程序员", "公务员")

for name, age, job in zip(names, ages, jobs):
    print("{0}--{1}---{2}".format(name, age, job))
