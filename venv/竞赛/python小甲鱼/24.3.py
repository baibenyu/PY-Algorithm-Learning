def age(num=4,a1=10,interval=2):
    if num > 0:
        num -= 1
        return age(num,a1+interval,interval)
    else:
        return a1
    
    
