import math

def snt(n):
    n = int(n)
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if(n % i == 0):
            return False
    return True

t = int(input())
while(t > 0):
    t = t - 1
    s = input()
    countPrime = 0
    countNotPrime = 0
    for i in s:
        if(snt(int(i))):
            countPrime = countPrime + 1
        else:
            countNotPrime = countNotPrime + 1
    if(countPrime > countNotPrime and snt(len(s))):
        print("YES")
    else:
        print("NO")