def sequence(x):
    if x<3:
        return 1
    else:
        return sequence(x-1)+sequence(x-2)
