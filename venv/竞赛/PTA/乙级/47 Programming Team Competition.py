# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/19 11:30'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    scores = [0 for i in range(1001)]
    for i in range(n):
        team, score = input().split()
        team = team.split("-")
        scores[int(team[0])] += int(score)

    print(scores.index(max(scores)), max(scores))

    end = time.perf_counter()
    print(end - start)
