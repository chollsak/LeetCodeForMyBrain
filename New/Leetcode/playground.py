def findFact(n):
    if n == 0:
        return 1
    else:
        return n * findFact(n - 1)

print(findFact(5))
print(5*4*3*2*1)