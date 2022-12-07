from math import gcd

s = input().split()
l = int(s[0])
r = int(s[1])
for i in range(l, r - 1):
    for j in range(i + 1, r):
        if(gcd(i, j) == 1):
            for k in range(j + 1, r + 1):
                if(gcd(i, k) == 1 and gcd(j, k) == 1):
                    print(f"({i}, {j}, {k}) ")