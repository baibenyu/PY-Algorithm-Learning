def sum_up(prime_number=20000):
    sum = 0
    for i in range(2, prime_number + 1):
        judge = True
        for each in range(2, i ):
            if i % each == 0:
                judge = False
                break

        if judge:
            sum += i
    yield sum


for z in sum_up():
    print(z)
