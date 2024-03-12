def btx(x):
    temp=""
    while x != 0:
        temp = str(x % 2)+temp
        x = x//2
    return temp
    
    
