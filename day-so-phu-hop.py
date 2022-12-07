
t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    b = [int(i) for i in input().split()]
    b.sort()
    kt = True
    for i in range(n):
        if(a[i] > b[i]):
            kt = False
            break
    print("YES") if kt else print("NO")