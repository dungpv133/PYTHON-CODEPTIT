
def kt(n):
    ngay = int(n[0])
    thang = int(n[1])
    if(thang == 1):
        if(ngay < 20):
            return "Ma Ket"
        else:
            return "Bao Binh"
    if(thang == 2):
        if(ngay < 19):
            return "Bao Binh"
        else:
            return "Song Ngu"
    if(thang == 3):
        if(ngay < 21):
            return "Song Ngu"
        else:
            return "Bach Duong"
    if(thang == 4):
        if(ngay < 20):
            return "Bach Duong"
        else:
            return "Kim Nguu"
    if(thang == 5):
        if(ngay < 21):
            return "Kim Nguu"
        else:
            return "Song Tu"
    if(thang == 6):
        if(ngay < 21):
            return "Song Tu"
        else:
            return "Cu Giai"
    if(thang == 7):
        if(ngay < 23):
            return "Cu Giai"
        else:
            return "Su Tu"
    if(thang == 8):
        if(ngay < 23):
            return "Su Tu"
        else:
            return "Xu Nu"
    if(thang == 9):
        if(ngay < 23):
            return "Xu Nu"
        else:
            return "Thien Binh"
    if(thang == 10):
        if(ngay < 23):
            return "Thien Binh"
        else:
            return "Thien Yet"
    if(thang == 11):
        if(ngay < 23):
            return "Thien Yet"
        else:
            return "Nhan Ma"
    if(thang == 12):
        if(ngay < 22):
            return "Nhan Ma"
        else:
            return "Ma Ket"

def main():
    t = int(input())
    while(t > 0):
        t -= 1
        print(kt(input().split()))

if(__name__ == "__main__"):
    main()