# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/21 15:14'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n, k = map(int, input().split())
    wrong = [0 for _ in range(k)]
    questions = []
    for i in range(k):
        questions.append(input().split())
    students = []
    for j in range(n):
        temp = input().replace(" ", "")
        temp = temp.replace("(", "")
        temp = temp.split(")")
        score = 0
        for x in range(len(temp) - 1):
            if temp[x][0] == questions[x][2]:
                if temp[x][1:] == "".join(questions[x][3:]):
                    score += int(questions[x][0])
                else:
                    wrong[x] += 1
            else:
                wrong[x] += 1
        print(score)
    maxwrong = max(wrong)
    if maxwrong == 0:
        print("Too simple")
    else:
        print(maxwrong, end = " ")
        ans = []
        for y in range(len(wrong)):
            if wrong[y] == maxwrong:
                ans.append(y + 1)
        for each in ans[:-1]:
            print(each, end = " ")
        print(ans[-1])

    end = time.perf_counter()
    print(end - start)
