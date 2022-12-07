
#b1
# def description_city(city, country = 'Vietnam'):
#     print(f"{city.title()} la thanh pho cua {country.title()}")

# city_name = input("Nhap thanh pho: ")
# country_name = input("Nhap quoc gia: ")
# description_city(city_name, country_name)
# city_name = input("Nhap thanh pho: ")
# description_city(city_name)

#bai2

# def maxof3(num1, num2, num3):
#     if(num1 == num2 and num1 == num3):
#         return num1
#     elif(num1 > num2 and num1 > num3):
#         return num1
#     elif(num2 > num1 and num2 > num3):
#         return num2
#     else:
#         return num3

# def giaithua(n):
#     if n == 0:
#         return 1
#     res = 1
#     for i in range(2, n + 1):
#         res *= i
#     return res

# print(maxof3(1, 5, 10))
# print(giaithua(5))

#bai4
# def cocunt_chars(string):
#     print(f"So chu thuong: {sum([int(c.islower()) for c in string])}") 
#     print(f"So chu hoa: {sum([int(c.isupper()) for c in string])}") 

# sentence = input()
# cocunt_chars(sentence)

#bai5

# def distance_from_zero(n):
#     if(type(n) == int or type(n) == float):
#         return abs(n)
#     else:
#         return 'Nope'
# print(distance_from_zero(9))

#bt1

# def multiple(list):
#     result = 1
#     for num in list:
#         result *= int(num)
#     return result
# list = [8, 2, 3, -1, 7]
# print(multiple(list))

#bt2

# def make_car(brand, type, **kwargs):
#     kwargs['brand'] = brand
#     kwargs['type'] = type
#     return kwargs
# print(make_car('hyundai', 'kona', color = 'red', bks = '29a112345'))

#bt3

# def luythua(x, y):
#     if(x < 0 or y < 0):
#         return 0
#     res = 1
#     for num in range(1, y + 1):
#         res *= x
#     return res

# x = int(input("Nhap so x: "))
# y = int(input("Nhap so y: "))
# print(f"Luy thua cua x mu y la: {luythua(x, y)}")

#bt4

# def check_perfect_number(n):
#     sum = 0
#     for num in range(1, n - 1):
#         if(n % num == 0):
#             sum += num
#     if(sum == n):
#         return 1
#     return 0

# n = int(input("Nhap vao mot so: "))
# if(check_perfect_number(n)):
#     print(f"{n} la so hoan hao")
# else:
#     print(f"{n} khong la so hoan hao")