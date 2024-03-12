grade=input("请输入成绩:")
while not grade.isdigit():
    grade=input("请输入阿拉伯数字")
grades=int(grade)
if grades>90:
    print("A")
elif grades>80:
    print("B")
elif grades>=60:
    print("C")
else:
    print("D")
