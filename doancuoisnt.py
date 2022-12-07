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
    num = int(n[-4 : ])
    return prime(num)

    
t = int(input())
while((t > 0)):
    t -= 1
    s = input()
    if(pos(s)):
        print("YES")
    else:
        print("NO")