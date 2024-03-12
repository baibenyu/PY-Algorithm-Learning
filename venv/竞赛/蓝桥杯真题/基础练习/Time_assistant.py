# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/2 9:13'

while True:
    try:  # 难点在于耐心与细心,健壮性要好
        dict1 = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                 9: "nine",
                 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
                 17: "seventeen",
                 18: "eighteen", 19: "nineteen", }
        dict2 = {0: "zero", 10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty"}
        h, m = map(int, input().strip().split())
        if m == 0:
            if h in dict1:
                print(dict1[h] + " o'clock")
            elif h in dict2:
                print(dict2[h] + " o'clock")
            else:
                ones = h % 10
                tens = h - ones
                print(dict2[tens] + " " + dict1[ones] + " o'clock")
        else:
            if h in dict1:
                print(dict1[h], end = " ")
            elif h in dict2:
                print(dict2[h], end = " ")
            else:
                ones = h % 10
                tens = h - ones
                print(dict2[tens] + " " + dict1[ones], end = " ")
            if m in dict1:
                print(dict1[m])
            elif m in dict2:
                print(dict2[m])
            else:
                ones = m % 10
                tens = m - ones
                print(dict2[tens] + " " + dict1[ones])
    except BaseException as e:
        print(e)
