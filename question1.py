from timeit import default_timer as timer

def sumofN(input):
    sum = 0
    for a in range(1, input+1):
        sum += a
    return sum

start = timer()
first = sumofN(10)
end = timer()
print(end - start)

start = timer()
second = sumofN(10000)
end = timer()
print(end - start)

start = timer()
third = sumofN(1000000)
end = timer()
print(end - start)

start = timer()
fourth = sumofN(1000000000)
end = timer()
print(end - start)






