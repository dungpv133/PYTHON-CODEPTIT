
#bt1
# filename = "guest.txt"

# with open(filename, 'a+') as file:
#     while(True):
#         ten = input("Nhap vao ten cua ban: ")
#         if(ten == "quit"):
#             break
#         print(f"Xin chao {ten}")
#         file.write(f"{ten} \n")
#     lines = file.read()  
# print(lines)

#bt2
# filename = "responses.txt"
# with open(filename, 'a+') as file:
#     while(True):
#         lydo = input("Ly do ban thich hoc lap trinh: ")
#         if(lydo == ''):
#             break
#         file.write(lydo + "\n")
#     lines = file.read()
# print(lines)
    

#bt3
# while(True):
#     num = input("Nhap vao mot so: ")
#     if(num == "quit"):
#         break
#     try:
#         print(f"So ban vua nhap la: {int(num)}")
#     except ValueError:
#         print("Hay nhap vao so ")

#bt4
# filenames = ["guest.txt", "responses.txt", "testpy.txt"]
# for file in filenames:
#     try:
#         with open(file, 'r') as readfile:
#             str = ""
#             for f in readfile:
#                 str += " " + f.strip()
#             str = str.split()
#             print(f"So tu trong file {file} la: {len(str)}")
#     except FileNotFoundError:
#         print(f"File {file} khong ton tai")

#bt5
# import collections
# import json
# dicts = {"num1" : 20, "aabb" : 15, "zzz" : 1, "bbbb" : 113}
# ordered_dicts = collections.OrderedDict(sorted(dicts.items()))
# filename = "sortdict.json"
# with open(filename, 'a+') as f:
#     json.dump(ordered_dicts, f)

#bt6
# import json
# def greet_user(filename):
#     try:
#         with open(filename, 'r') as f:
#             name = json.load(f)
#     except FileNotFoundError:
#         name = input("Hay nhap ten cua ban: ")
#         with open(filename, 'a+') as f:
#             json.dump(name, f)
#             print(f"Xin chao {name}")
#     else:
#         print(f"Rat vui duoc gap lai {name}")

# ten_file = "username.json"
# greet_user(ten_file)
