#bai1

# ques  = int(input("Nhap so nguoi muon dat ban: "))
# if(ques > 8):
#     print("Vui long cho")
# else:
#     print("Ban da san sang")


#bai2

# so = int(input("Nhap vao mot so: "))
# if(so % 10 == 0):
#     print(f"{so} la boi so cua 10")
# else:
#     print(f"{so} khong la boi so cua 10")

#bai3

# num_list = [100, 1, 10, 9, 100, 100, 89, 50, 100]
# i = 0
# while i < len(num_list):
#     if num_list[i] == 100:
#         print(f"100 in position: {i}")
#     i += 1


#bai4

# chuoi = input("Nhap vao mot danh sach: ").split(" ")

# i = 0
# kq = []
# while i < len(chuoi):
#     if(chuoi[i] != ""):
#         kq.append(chuoi[i])
#     i += 1
# print(kq)

#bai5

# n = int(input("Nhap so n: "))
# fibo = [0, 1]
# i = 1
# temp = 1
# while temp <= n:
#     i += 1
#     temp = fibo[i - 1] + fibo[i - 2]
#     if(temp <= n):
#         fibo.append(temp)
# print(fibo)

#bai6

# chuoi = input("Nhap chuoi nhi phan: ").split(",")
# nhi = []
# for i in chuoi:
#     if(i != ""):
#         nhi.append(i)
# for i in nhi:
#     num = 0
#     for j in range(len(i)):
#         if(i[j] == '1'):
#             num += pow(2, j)
#     if(num % 5 == 0):
#         print(i)

#bai7

n = 30
prime_numbers = [2,3]
i=3
while (True):
        i+=1
        status = True
        for j in range(2,int(i/2)+1):
            if(i%j==0):
                status = False
                break
        if(status==True):
            prime_numbers.append(i)
        if(len(prime_numbers)==n):
            break
print('So nguyen to thu 30 la:', prime_numbers[n-1])
