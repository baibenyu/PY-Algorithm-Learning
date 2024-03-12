def gcd(x,y):
    large=max(x,y)
    small=min(x,y)
    remainder=large % small
    if remainder == 0:
        return small
    else:
        return gcd(small,remainder)
