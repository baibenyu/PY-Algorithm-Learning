temp=int(input(":"))
queue1=1
queue2=1
queue3=0
for each in range(temp-2):
    queue3=queue1+queue2
    queue1=queue2
    queue2=queue3
print(queue3)
    
