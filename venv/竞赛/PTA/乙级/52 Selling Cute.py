# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/20 15:11'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    hands = input().replace("]", "").split("[")[1:]
    eyes = input().replace("]", "").split("[")[1:]
    mouths = input().replace("]", "").split("[")[1:]
    k = int(input())
    for i in range(k):
        nums = list(map(int, input().split()))
        if 1 <= nums[0] <= len(hands) and 1 <= nums[4] <= len(hands) and 1 <= nums[1] <= len(eyes) and 1 <= nums[
            3] <= len(eyes) and 1 <= nums[2] <= len(mouths):
            print(hands[nums[0] - 1] + "(" + eyes[nums[1] - 1] + mouths[nums[2] - 1] + eyes[nums[3] - 1] + ")" + hands[
                nums[4] - 1])
        else:
            print("Are you kidding me? @\/@")

    end = time.perf_counter()
    print(end - start)
