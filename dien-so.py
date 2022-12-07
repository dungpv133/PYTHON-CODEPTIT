

t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    count = 0
    for i in range(1, n):
        if(a[i] - a[i - 1] > 1):
            count += a[i] - a[i - 1] - 1
    print(count)