
t = int(input())
while(t > 0):
    t -= 1
    a = input().split(".")        
    kt = True
    # print(a)
    if(len(a) != 4):
        kt = False
    else:
        for i in a:
            if(not i.isnumeric()):
                kt = False
                break
            else:
                i = int(i)
                if(i < 0 or i > 255):
                    kt = False
                    break
    print("YES") if kt else print("NO")