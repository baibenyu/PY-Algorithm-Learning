# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/2 8:54'

while True:
    # try:
    string1 = input().strip()
    string2 = input().strip()
    if len(string1) != len(string2):
        print(1)
    elif string1 == string2:
        print(2)
    elif string1.upper() == string2.upper():
        print(3)
    else:
        print(4)
# except BaseException as e:
#     print(e)
