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
    for i in range(0, len(n), 2):
        if(int(n[i]) % 2 != 0):
            return False 
    for i in range(1, len(n), 2):
        if(int(n[i]) % 2 == 0):
            return False
    sum = 0
    for i in n:
        sum += int(i)
    if(not prime(sum)):
        return False
    else:
        return True

    
t = int(input())
while((t > 0)):
    t -= 1
    s = input()
    if(pos(s)):
        print("YES")
    else:
        print("NO")