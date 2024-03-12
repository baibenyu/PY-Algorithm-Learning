class Trace:
    x = 0
    def __init__(self):
        Trace.x += 1

    def __del__(self):
        Trace.x -= 1


t = Trace()
r = Trace()
a = Trace()
print(Trace.x)
del r
print(Trace.x)