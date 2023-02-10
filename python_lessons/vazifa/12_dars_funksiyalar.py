"""
Thame: Funkcions(Funksiyalar)
"""

""" Javoblar """

""" 1)
    Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
"""
# def salom_ber() :
#     """" Foydalanuvchi tug'ilgan yilini hisolaydigan funksiya"""
#     ism = input("Ismingiz nima ?")
#     yosh = int(input(f"{ism.title()} yoshingiz nechida ?"))
#     print(f"Assalomu aleykum {ism.title()}. Siz {2023-yosh} da tug'ilgansiz.")

# salom_ber()


""" 2)
    Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
"""
# def daraja() :
#     """Sonni darajaga ko'taruvchi funksia"""
#     son = int(input("Istalgan butun son kiriting: "))
#     daraja_son = int(input(f"{son} ni nechanchi darajaga ko'tarishni hohlaysiz: "))
#     if son and daraja_son > 0 :
#         print(f"{son} ning {daraja_son}-darajasi, {son**daraja_son} ga teng.")        
# daraja() 

# def daraja2() :
#     """Sonni darajaga ko'taruvchi funksia"""
#     son = int(input("Istalgan butun son kiriting: "))
#     print(f"{son} ning kvadrati {son**2} ga, kubi esa {son**3} ga teng")
# daraja2()

""" 3)
    Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# """
# def toq_juft() :
#     """Sonni toq yoki juft ekanini aniqlaydigan funksia"""
#     son = int(input("Istalgan butun sonni kiriting: "))
#     if son%2==0:
#         print(f"{son} juf son")
#     else:
#         print(f"{son} toq son")

# toq_juft()


""" 4)
    Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
    Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
"""
# def katta_kichik():
#     """Kiritilgan sonning eng kattasini ko'rsatuvchi funksia """
#     while True:
#         son1 = input("1- sonni kiriting: ")
#         son2 = input("2- sonni kiriting: ")
#         if son1.isdigit() and son2.isdigit():
#             if int(son1) > int(son2):
#                 print(f"{son1}")
#             elif int(son1) < int(son2):
#                 print(f"{son2}")
#             else:
#                 print("Sonlar teng")
#             break
#         else:
#             print("Siz son kiritmdingiz!!!")
# katta_kichik()


""" 5)
    Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz 
    bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
"""
# def bolinish() :
#     """berilgan sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksia """
#     son = int(input("Istalgan butun sonni kiriting: "))
#     for n in range(2,11):
#         if  son%n==0 :
#             print(f"{son} {n}ga qoldiqsiz bo'linadi")
# bolinish()


""" 6)
    Foydalanuvchidan uning oila azolari haqidagi malumotlarmni olib ularni konsulga chiqaruvchi funksiya 
    yozing. M: ismi, yoshi, kasbi...   
"""
# def family(name, surname, age, work):
#     print(f"{name.title()} {surname.title()} yoshi {age} da. Kasbi  {work.title()}")
    
# family("Aziz", "Aliyev", 23, "Dasturchi")
# family("Bonu", "ALiyeva", 22, "Hamshira")
# family("Otabek", "Aliyev", 45, "Muhandis")
# family("Olim", "dfsdf", 23, 'SFSF') 
       

""" 7)
    Tog'ri to'rtburchakli uchburchakning katetlarini qabul qilib olib uning gipotenuzsini hisoblovchi funksiya 
    yozing, 2- katetni o'zgarmas parameter sifatida bering.
"""
# from math import sqrt
# def tbu(k1, k2=5):
#     g = round(sqrt(k1**2+k2**2),2)
#     print(f"Katetlari {k1} va {k2} ga teng TBU ning gipotenuzasi taxminan {g} ga teng")

# tbu(k2=6, k1=4)
# tbu(6,5)
# tbu(3)
