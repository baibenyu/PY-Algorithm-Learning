# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/2 10:41'

while True:
    # try:
    v1, v2, t, s, l = map(int, input().strip().split())
    r_distance, t_distance, count = 0, 0, 0
    while r_distance < l and t_distance < l:
        if r_distance - t_distance >= t:
            t_distance += v2 * s
            count += 1
        else:
            r_distance += v1
            t_distance += v2
    if r_distance > t_distance:
        print("R")
        print("{:.0f}".format(l / v1 + count * s))
    elif r_distance < t_distance:
        print("T")
        print("{:.0f}".format(l / v2))
    else:
        print("D")
        print("{:.0f}".format(l / v2))
    # except BaseException as e:
    #     print(e)
