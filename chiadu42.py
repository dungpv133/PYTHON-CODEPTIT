

t = 10
res = set()
while(t > 0):
    s = input().split()
    for i in s:
        res.add(int(i) % 42)
    t -= len(s)
# print(res)
print(len(res))
