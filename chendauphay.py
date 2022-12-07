


t = 1
while(t > 0):
    t -= 1
    s = input()
    s = s[::-1]
    # print(s)
    res = ""
    for i in range(0, len(s)):
        res = res + s[i]
        if(i % 3 == 2 and i != len(s) - 1):
            res = res + ','
    print((res[:: -1]))