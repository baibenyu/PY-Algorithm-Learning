def gcd(x,y):
    large = max(x,y)
    small = min(x,y)
    mod = large % small
    while mod != 0:  
        mod = large % small
        large = small
        small = mod
    return large
