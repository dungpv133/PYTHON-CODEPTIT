
def kt(arr):
    return arr[0] == arr[1] and arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3]
        

while(True):
    a = list(int(i) for i in input().split())
    if(kt(a) and a[0] == 0 ):
        break
    count = 0
    while(kt(a) == False):
        count += 1
        num = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(a[3] - num)
    print(count)
    