import math

t = int(input())
while(t > 0):
    t -= 1
    s = input()
    kt = True

    for i in range(1, len(s)):
        if(abs(int(s[i]) - int(s[i - 1])) != 2):
            # print((int(s[i]) - int(s[i - 1])))
            kt = False
            break
    if(kt):
        sum = 0
        for i in s:
            sum += int(i)
        # print(sum)
        if(sum % 10 != 0):
            kt = False
    if(kt):
        print("YES")
    else:
        print("NO")