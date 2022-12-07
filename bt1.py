#bai1

# chuoi = "ghi abc def 123"
# xau = chuoi.split(" ")
# xau = sorted(xau)
# print(xau)

#bai2

# chuoi = "abc123aagha8a"
# key = chuoi[0]
# res = ""
# for i in range(0, len(chuoi)):
#     if chuoi[i] == key:
#         res = res + "$"
#     else:
#         res = res + chuoi[i]
# print(res)

#bai3

from typing import List


# chuoi = "123 abc ghijkl"
# res = ""
# for i in range(0, len(chuoi)):
#     if(i % 2 == 0):
#         res = res + chuoi[i]
# print(res)

#bai4

# List = ['abcda', 'xyz', 'ssss', 1236, 1211]
# dem = 0
# for i in List[0 : ]:
#     temp = str(i)
#     if len(temp) > 2 and temp[0] == temp[-1]:
#         dem +=1
# print(dem)

#bai5

# List = ['a', 'b']
# n = 4
# res = []
# for i in range(1, n + 1):
#     for j in  List[0 : ]:
#         temp = j + str(i)
#         res.append(temp)
# print(res)
    


#bai6

# List = [38, 12, 55]
# List = sorted(List, reverse=True)
# res = ""
# for i in List[0 : ]:
#     temp = str(i)
#     res = res + temp
# print(res)


#bai7

# List = [[1, 2, 3], [4, 5, 6], [10, 11, 12]]
#C1: print(max(List, key = sum))
#C2: Sum = [sum(i) for i in List]
#index_max = Sum.index(max(Sum))
#print(Lis[index_max])
#C3: 
# pos = 0
# max_sum = 0
# for i in range(0, len(List)):
#     sum = 0
#     for j in range(0, len(List[i])):
#         sum += List[i][j]
#     if(sum > max_sum):
#         max_sum = sum
#         pos = i
# print(List[pos])

#bai8

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#             [7, 8, 9]]
# tong = 0
# tich = 1
# for i in range(len(matrix)):
#     tong += int(matrix[i][i])
#     tich *= int(matrix[i][i])
# print(f"{tong}  {tich} ")

#bai9
# import collections
# string = "programming"
# f = collections.Counter(list(string))
# res = dict(f)
# print(res)
#bai10

# list_key = ['a', 'b', 'c', 'd']
# list_value = [1, 2, 3, 4]
# dict_new = {}
# for i in range(0 , len(list_key)):
#      dict_new[list_key[i]] = list_value[i]
# print(dict_new)


#bai11

# cau = "mot hai 3 4. hai 4 nam mot hai. 4 muoi bay tam tam mot mot mot."
# cau = cau.replace('.', '')
# tu = cau.split()
# kq = {}
# for i in tu:
#     if i not in kq and cau.count(i) > 2:
#         kq[i] = cau.count(i)
# print(sorted(kq, reverse=True))


