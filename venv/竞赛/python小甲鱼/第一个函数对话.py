def myfirstbot(x):
    talkback = x[:(len(x) - 1)]
    print(talkback)
    log = input(':')
    return talkback

myfirstbot("你好")