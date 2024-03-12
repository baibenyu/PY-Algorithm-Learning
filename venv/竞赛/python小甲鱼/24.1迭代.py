def get_digits(n):
    length = len(str(n))
    temp = []
    for i in range(length):
        remainder = n//(10**i)%10
        temp.append(remainder)
    temp.reverse()
    return temp
        
        
