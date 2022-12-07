
import math

n = int(input())
a = [int(i) for i in input().split()]
count = 1000000000
val = a[0]
for i in a:
    dem = 0
    for j in a:
        if(i == j):
            continue
        else:
            dem += abs(i - j)
    if(dem < count):
        count = dem
        val = i
print(f"{count} {val}")