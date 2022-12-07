import math

def snt(n):
    n = int(n)
    if(n < 2): 
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if(n % i == 0):
            return False
    return True

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    count = 0
    for i in a:
        if(not snt(i)):
            n1, n2 = 0, 0
            while(not snt(i + n1)):
                n1 += 1
            while(not snt(i - n2)):
                n2 += 1
            # print(f"{n1} {n2} ; {i}")
            if(count < min(n1, n2)):
                count = min(n1, n2)
    print(count)

if(__name__ == "__main__"):
    main()

