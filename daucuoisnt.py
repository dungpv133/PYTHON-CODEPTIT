import math

def prime(n):
    num = int(n)
    if(num < 2):
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if(num % i == 0):
            return False
    return True

def pos(n):
    dau = int(n[ : 3])
    cuoi = int(n[-3 : ])
    return prime(dau) and prime(cuoi)    

    
t = int(input())
while((t > 0)):
    t -= 1
    s = input()
    if(pos(s)):
        print("YES")
    else:
        print("NO")