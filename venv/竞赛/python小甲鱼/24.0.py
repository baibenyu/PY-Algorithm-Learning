def btx(x):
    if x == 1:
        return "1"
    else:
        return str(x%2)+btx(x//2)
