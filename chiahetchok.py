chuoi = input().split()
a = int(chuoi[0])
k = int(chuoi[1])
n = int(chuoi[2])
res = []
count = 0
while(True):
    count += 1
    if(k * count > n):
        break
    if(k * count - a > 0):
        res.append(k * count - a)

if(len(res) == 0):
    print(-1)
else:
    for i in res:
        print(i, end = ' ')
print()

