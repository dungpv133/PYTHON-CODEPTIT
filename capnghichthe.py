
n = int(input())
mang1 = input()
mang1 = mang1.split(' ')
count = 0
for i in range(0, n - 1):
    #print(mang1[i])
    for j in range (i + 1, n):
        if int(mang1[i]) > int(mang1[j]) :
            count += 1
            #print(mang1[i] + " " + mang1[j])

print(count)
