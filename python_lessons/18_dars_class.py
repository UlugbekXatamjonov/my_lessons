"""
Thame: Classlar bilan ishlash
"""
""" Classlarga argument sifatida turli ma'lumot turlarini uzatish """
# class Student:
#     """ O'quvchi classi """
#     def __init__(self, full_name, year, marks, friends):
#         """ Student haqidagi malumotlarni o'zida saqlovchi funksiya """
#         self.full_name = full_name
#         self.year = year
#         self.marks = marks
#         self.friends = friends
        
#     def get_name(self):
#         return self.full_name
    
#     def get_info(self):
#         return f"{self.full_name}ning yoshi {self.year}"
        
#     def get_marks(self):
#         print(f"{self.full_name}ning baxolari:")
#         for key, value in self.marks.items():
#             print(f"{key.capitalize()} dan {value}")   
    
#     def get_friends(self):
#         print(f"{self.full_name}ning do'stlari:")
#         for ism in  self.friends:
#             print(f"{ism}", end = " ")
        
        
# baxolar = {
#     'matematika':3, 
#     "ingliz_tili":5, 
#     "ona_tili":5, 
#     "geografiya":4
# }
# friends = ['Ali', "Olim", "Hasan", "Husan", "Vali"]


# student1 = Student("Boburov", 1999, baxolar, friends)
# student2 = Student("Nodira Jamilova", 2002, {'matematika':5, 
#                                             "ingliz_tili":4, 
#                                             "ona_tili":3, 
#                                             "geografiya":5
#                                         }, ['Guli', "Aziza", "Husnora", "Madina", "Barno"])

# print(student2.get_name())
# print(student2.get_info())

# print(student2.get_marks())
# print(student2.get_friends())


""" Classlarga standart qiymat berish  """
# class Student:
#     """ O'quvchi classi """
#     def __init__(self, full_name, age, level, fan="Ingliz tili"):
#         """ Student haqidagi malumotlarni o'zida saqlovchi funksiya """
#         self.full_name = full_name
#         self.age = age
#         self.level = level
#         self.fan = fan

#     def get_info(self):
#         return f"{self.full_name} {self.age} yoshda va {self.level}-bosqich talabasi. Yo'nalishi {self.fan}"

#     def set_level(self):
#         self.level  = self.level + 1
#         return self.level
    
#     def set_age(self):
#         self.age = self.age + 1
#         return self.age
    
#     def set_fan(self, yangi_fan):
#         self.fan = yangi_fan
#         return f"{self.full_name}ning yo'nalishi {self.fan} ga o'zgartirildi."
    

# student1 = Student("Asadbek Olimov", 24, 1, "Matemetika")
# student2 = Student("Guli Azimova", 22, 3)

# print(student1.get_info())
# print(student2.get_info())

# print(student1.set_age(), student1.set_level())
# print(student2.set_age(), student2.set_level())

# print(student1.set_fan("Geometriya"))
# print(student2.set_fan("Rust tili"))

# print(student1.get_info())
# print(student2.get_info())


""" 
Vazifa:

1) Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar
    (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart 
    qiymat bering (masalan, kilometer=0). Avto ga oid obyektning xususiyatlarini qaytaradigan 
    metodlar yozing. get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
    Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
    update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
"""




