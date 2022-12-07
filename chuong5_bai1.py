#bt1\
# student = {'ten' : 'dungx', 'msv' : 'B19DCCN133', 'lop' : 'D19CQCN01-B'}
# student['mon'] = "Lap trinh Python"
# print(student)

#bt2

# list = ['a', 1, 1, 'b', 4, 4, 'a', 2]
# result = {}
# for i in list:
#     if i not in result:
#         result[i] = 1
#     else:
#         result[i] += 1
# print(result)

#bt3

# dict_key = {}
# for i in range (1, 16):
#     dict_key[i] = i ** 2
# print(dict_key)

#bt4

# dict_random = {1 : 'A', 2 : "ABC", 3 : 100, 4 : 20, 5 : 'abc def', 6 : 7, 7 : 13}
# sum = 0
# for value in dict_random.values():
#     if(str(value).isnumeric()):
#     #if type(value) == int or type(value) == float
#         sum += value
        
# print(f"Tong : {sum}")

#bt5

d1 = {'a' : 100, 'b' : 200, 'c' : 300}
d2 = {'a' : 300, 'b' : 200, 'd' : 400}
for key in d1.keys():
    if key in d2.keys():
        d1.update({key : d1[key] + d2[key]})

for key in d2.keys():
    if key not in d1.keys():
        d1[key] = d2[key]
print(d1)

#bt6

lst = {'a' : 1, 'b' : 20, 'c' : 'abc', 'd' : [1, 2, 3, 4], 5 : [1, 10, 30]}
count = 0
for i in lst.values():
    if(type(i) == list):
        count += 1
print(count)
