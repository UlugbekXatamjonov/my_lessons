"""
Thame: try-except
"""

""" Javoblar """

"""
1) Sonlar deb nomlangan ro'yhat tuzing ro'yhatda bir nechta sonlar va 0 ham bo'lsin.
    Keyin foydalanuvchidan biror son kiritishini so'rab, qabul qilingan sonni sonlar ro'yhatidagi 
    sonlarga bo'ling va natijani konsulga chiqaring.
    Dastur tuzishda 'try-except' dan foydalaning va yuzaga kelishi mumkin bo'lgan barcha xatoliklarni oldini oling !
"""
# sonlar  = [3,6,23,0,-7,81,-22]
# try:
#     son = int(input("Biror son kiring: "))
#     for x in sonlar:
#         if x == 0:
#             continue
#         else:
#             print(f"{son} / {x} = {son/x}")
# except:
#     print("Xato matni")

"""
2) Foydalanuvchidan uning yoshini qabul qilib olib uni 0 dan 1,000 gacha bo'lgan sonlardan qaysilariga 
    qoldiqsiz bo'linnishini aniqlab, qoldiqsiz bo'linadigan sonlarni ro'yhatga saqlab konsulga chiqaring.
    Va bu dasturni funksiyaga joylang. Hamda uni yozishda 'try-except' dan foydalaning va yuzaga kelishi
    mumkin bo'lgan xatoliklarni oldini oling
"""
# def func():
#     sonlar = list(range(0,1000))
#     x_sonlar = []

#     try:
#         yosh = int(input("Iltimos yoshingizni kiriting: "))
    
#         for son in sonlar:
#             if son != 0:
#                 if son%yosh == 0:
#                     x_sonlar.append(son)

#         print(f"Sizning yoshingiz {yosh}da va bu {yosh} soni quyidagi sonlarga qoldiqsiz bo'linadi: ")
#         for x in x_sonlar:
#             print(x, end = " ")
    
#     except ValueError:
#         print("Siz son kiritmadingiz !!!")
#     except ZeroDivisionError:
#         print("Xatolik yuzaga keldi")        
# func()

"""
3) To'g'ri burchakli uchburchakning gipotenuzasini hisoblash. Ushbu kodda yuzaga kelishi mumkin bo'lgan hatoliklarni
    'try-except' yordamida oldini oling
    
a = int(input("Birinchi katetni kiriting: "))
b = int(input("Ikkinchi katetni kiriting: "))
# c**2=a**2+b**2

import math
c = round(math.sqrt(a**2+b**2),2)
print(f"Katetlari {a} va {b} ga teng bo'lgan uchburchakning giputenuzasi {c} ga teng")

"""
# try:
#     a = int(input("Birinchi katetni kiriting: "))
#     b = int(input("Ikkinchi katetni kiriting: "))
#     # c**2=a**2+b**2

#     import math
#     c = round(math.sqrt(a**2+b**2),2)
#     print(f"Katetlari {a} va {b} ga teng bo'lgan uchburchakning giputenuzasi {c} ga teng")
# except ValueError:
#     print("Siz son kiritmadingiz !!!")
# except:
#     print("xatolik yuzaga keldi")

"""
4) mevalar deb nomlangan ro'yhat(list ) yarating. Avval uni o'zgarmas ro'yhat turiga , keyin esa set turiga o'zgartiring va konsulga ularning 
turini chiqaring.
	-remove() yordamida 3 ta discard() yordamida 3 ta elementni o'chirib tashlang va ro'yhatni konsulga chiqaring.
	-va yangi 5 ta element qo'shing va ro'yhatni konsulga chiqaring;
	-so'ngra ro'yhatni tozalang va uni konsulga chiqaring;
	-keyin esa ro'yhatni o'chirib tashlang;
 
    Ushbu kodda yuzaga kelishi mumkin bo'lgan hatoliklarni 'try-except' yordamida oldini oling

"""
# try:
#     mevalar = ['olma', 'anor', 'bexi', 'olcha','limon','qovun','torvuz']
#     mevalar = tuple(mevalar)
#     print(type(mevalar))
#     mevalar = set(mevalar)
#     print(type(mevalar))

#     mevalar.remove("olma")
#     mevalar.remove("anor")
#     mevalar.remove("bexi")
#     mevalar.discard("olcha")
#     mevalar.discard("limon")
#     mevalar.discard("qovun")
#     print(mevalar)

#     mevalar.add("gilos")
#     mevalar.add("o'rik")
#     mevalar.add("kiwi")
#     mevalar.add("apelsin")
#     mevalar.add("xurmo")
#     print(mevalar)

#     mevalar.clear()
#     print(mevalar)

#     del mevalar
#     print(mevalar)
# except NameError:
#     print("O'zgaruvchi nomi bilan xato yuzaga keldi")
# except:
#     print("Xato yuzaga keldi")









