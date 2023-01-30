"""
Thame: Operators va Boolens / Operatorlar
"""

"""
Vazifa:

‼️ Vazifada xatolar ustida ishlaymz. Bizga malum bir kodlar berilgan biz esa anashu kodlardagi xatolarni topishimiz va to'g'irlashimiz kerak bo'ladi. ‼️
"""

# 1)
# son = int(input("Juft son kiriting: "))
# if son%2!=0 :
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")

# 2)
# yosh = int(input("Yoshingiz nechida: "))
# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")

# 3)
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# 4) a)
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            

# 4) b)
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:" ))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)

# if bor_mahsulotlar:
#     print("Quidagi mahsulotlar do'konimizda bor")
#     for mahsulot in bor_mahsulotlar:
#         print(mahsulot)

# 5)
# users = ['alisher1983','aziza','yasina', 'umar']

# login = input("Yangi login tanlang:" )

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")
#     users.append(login)
# print(users)

# 6)
# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,son):
#     if not (son%n):
#         print(f"{son} son {n} ga qoldiqsiz bo'linadi ✅")
#     else:
#         print(f"{son} son {n} ga qoldiqli bo'linadi ❌")
        

# 7) Darsdavomida ko'rib o'tgan har bir operatorimizni(25 ta)  qatnashtirib mustaqil kodlar yozing
"""
"""


""" Javoblar """

""" 1 """
# son = int(input("Juft son kiriting: "))
# if son%2!= 0 :
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")        


""" 2 """
# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18 :
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")


""" 3 """
# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# if x==y :
#     print(f"{x}={y}")
# elif x<y :
#     print(f'{x}<{y}')
# else :
#     print(f"{x}>{y}")


""" 4 A """

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat :
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            


""" 4 B """
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:" ))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# for mahsulot in mavjud_emas:
#   print(mahsulot)


""" 5 """

# users = ['alisher1983','aziza','yasina' ,'umar']
# login = input("Yangi login tanlang:" )

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")


""" 6 """
# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,10000000000000000000000000):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")


""" 7 """
""" Mustaqil :) """

