coso = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

t = int(input())
for i in range(t):
    arr = [int(i) for i in input().split()]
    res = ""
    while(arr[0] > 0):
        num = str(coso[arr[0] % arr[1]])
        res += num
        arr[0] = arr[0] // arr[1]
    print(res[ :: -1])