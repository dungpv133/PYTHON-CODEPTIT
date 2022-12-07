

t = 1
while(t > 0):
    t -= 1
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    print(len(set(a)))