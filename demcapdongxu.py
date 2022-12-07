import math

n = int(input())
a = []
count = 0
hang = [0] * n
cot = [0] * n

for i in range(n):
    dong = input()
    for j in range(len(dong)):
        if(dong[j] == 'C'):
            hang[i] +=1
            cot[j] += 1
for i in range(n):
    if(hang[i] > 1):
        count += math.comb(hang[i], 2)
    if(cot[i] > 1):
        count += math.comb(cot[i], 2)
print(count)
        