
while(True):
    num = int(input())
    if(num == 0):
        break
    count = 1
    while(num != 1):
        count += 1
        if(num % 2 == 0):
            num = int(num / 2)
        else:
            num = int(num * 3 + 1)
    print(count)
    