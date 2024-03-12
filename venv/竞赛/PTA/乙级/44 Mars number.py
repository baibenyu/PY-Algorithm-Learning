# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/19 10:40'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    list1 = ["tret", "jan", "feb", "mar", "apr", "may", "jun", "jly", "aug", "sep", "oct", "nov", "dec"]
    list2 = ["tret", "tam", "hel", "maa", "huh", "tou", "kes", "hei", "elo", "syy", "lok", "mer", "jou"]
    dict1 = dict(zip(list1, [i for i in range(13)]))
    dict2 = dict(zip(list2, [i * 13 for i in range(13)]))
    for i in range(n):
        string = input()
        if string.isdigit():
            string = int(string)
            one, two = string % 13, string // 13
            if two != 0 and one != 0:
                print(list2[two], list1[one])
            elif two != 0 and one == 0:
                print(list2[two])
            elif two == 0 and one != 0:
                print(list1[one])
            else:
                print(list1[one])
        else:
            ans = 0
            string = string.split()
            for each in string:
                if each in dict1:
                    ans += dict1[each]
                elif each in dict2:
                    ans += dict2[each]
            print(ans)

    end = time.perf_counter()
    print(end - start)
