
t = int(input())
while(t > 0):
    t -= 1
    n, m, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    kt, idxA,idxB, idxC = 0, 0, 0, 0
    while(idxA < n and idxB < m and idxC < k):
        if(a[idxA] == b[idxB] == c[idxC]):
            print(a[idxA], end=" ")
            kt = 1
            idxA += 1
            idxB += 1
            idxC += 1
        elif a[idxA] < b[idxB]:
            idxA += 1
        elif b[idxB] < c[idxC]:
            idxB += 1
        else:
            idxC += 1
    if(not kt):
        print("NO")
    print()