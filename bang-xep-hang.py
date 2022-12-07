

class SinhVien:
    def __init__(self, ten, dung, submit):
        self.ten = ten
        self.dung = dung
        self.submit = submit
    
    def __str__(self):
        return self.ten + " " + str(self.dung) + " " + str(self.submit)

def compare(sv : SinhVien):
    dung = - sv.dung
    sub = sv.submit
    ten = sv.ten
    return (dung, sub, ten)    
a = []    
n = int(input())
for i in range(n):
    ten = input()
    dung, sub = [int(j) for j in input().split()]
    temp = SinhVien(ten, dung, sub)
    a.append(temp)
a = sorted(a, key = compare)
for i in a:
    print(i)