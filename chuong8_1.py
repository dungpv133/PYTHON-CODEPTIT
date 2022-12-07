#bt1, 2
# class User:
#     def __init__(self, first, last, gender, age):
#         self.first_name = first
#         self.last_name = last
#         self.gender = gender
#         self.age = age
#         self.login_attempts = 0
#     def description_user(self):
#         print(f"Info of user: \nName: {self.first_name} {self.last_name}")
#         print(f"Gender: {self.gender} \nAge: {self.age}")
#     def welcome_user(self):
#         print(f"Hello {self.first_name} {self.last_name}")
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#     def reset_login_attempts(self):
#         self.login_attempts = 0
    
# user1 = User('nguyen', 'a', 'male', 20)
# print(f"{user1.first_name}; {user1.last_name}; {user1.gender}; {user1.age}")
# user1.description_user()
# user1.welcome_user()
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)

#bt3

# class Student:
#     def __init__(self, ten, msv, lop):
#         self.ten = ten
#         self.msv = msv
#         self.lop = lop
#     def description_student(self):
#         print(f"Ten: {self.ten} \nMa sinh vien: {self.msv} \nLop: {self.lop}")
#     def description_object(self, mon):
#         print(f"Sinh vien {self.ten} ma sinh vien {self.msv} lop {self.lop} dang hoc mon {mon}")

# student1 = Student('ABC', 'B19DCCN001', 'D19CQCN01-B')
# student1.description_student()
# student1.description_object('Lap trinh Python')

#bt4

class Person:
    def __init__(self, ten, gt, sinh):
        self.ten = ten
        self.gt = gt
        self.sinh = sinh
    def description_person(self):
        print(f"Ten: {self.ten} \nGioi tinh: {self.gt} \nNgay sinh: {self.sinh}")

class Student(Person):
    def __init__(self, ten, gt, sinh, msv, dtb, mail):
        super().__init__(ten, gt, sinh)
        self.msv = msv
        self.dtb = dtb
        self.mail = mail
    def description_student(self):
        self.description_person()
        print(f"Ma sinh vien: {self.msv} \nDiem trung binh: {self.dtb} \nEmail: {self.mail}")
    def check_schorlaship(self):
        return float(self.dtb) >= 3.2
    
# student1 = Student('Nguyen Van A', 'nam', '01/01/2001', 'B19DCCN001', 3.3, 'aaa@gmail.com')
# student1.description_student()
# if(student1.check_schorlaship()):
#     print(f"Sinh vien {student1.ten} duoc hoc bong")
# else:
#     print(f"Sinh vien {student1.ten} khong duoc hoc bong")

class Rectangle:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def chuvi(self):
        return int(self.dai) * 2 + int(self.rong) * 2
    def dientich(self):
        return int(self.dai) * int(self.rong)

