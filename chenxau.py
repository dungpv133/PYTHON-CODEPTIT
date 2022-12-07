
s1 = input()
s2 = input()
pos = int(input())
for i in range(0, pos - 1):
    print(s1[i], end = "")
print(s2, end = "")
for i in range(pos - 1, len(s1)):
    print(s1[i], end = "")