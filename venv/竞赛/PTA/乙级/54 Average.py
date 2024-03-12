# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/21 10:28'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    nums = input().split()
    sumup = 0
    legal = 0

    for each in nums:
        try:
            temp = float(each)
            if "." in each:
                if len(each.split(".")[1]) <= 2:
                    if -1000.00 <= temp <= 1000.00:
                        legal += 1
                        sumup += temp
                    else:
                        print(f"ERROR: {each} is not a legal number")
                else:
                    print(f"ERROR: {each} is not a legal number")
            else:
                if -1000.00 <= temp <= 1000.00:
                    legal += 1
                    sumup += temp
                else:
                    print(f"ERROR: {each} is not a legal number")
        except:
            print(f"ERROR: {each} is not a legal number")
    if legal > 1:
        print(f"The average of {legal} numbers is {sumup / legal:.2f}")
    elif legal == 1:
        print(f"The average of {legal} number is {sumup / legal:.2f}")
    else:
        print(f"The average of 0 numbers is Undefined")

    end = time.perf_counter()
    print(end - start)
