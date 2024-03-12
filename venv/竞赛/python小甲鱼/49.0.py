def myRev(data):
    # 这里用range生成data的倒序索引
    # 注意，range的结束位置是不包含的
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

