"""
Thame: if-esle-elif operatorlari
"""


""" 
Vazifa:

1)
dastur: Assalomu aleykum do'konimizga hush kelibsiz !
dastur: Bizda quyidagi mahsulotlar bor: olma, anor, non, shakar, tuz, qaymoq
        Nechta mahsulot sotib olmoqchisiz ?
foydalanuvchi: 4
dastur: 1-mahsulotni kiriting:
foydalanuvchi: olma
dastur: 2-mahsulotni kiriting:
foydalanuvchi: non
dastur: 3-mahsulotni kiriting:
foydalanuvchi: sut
dastur: 4-mahsulotni kiriting:
foydalanuvchi: tuz
dastur: 5-mahsulotni kiriting:
foydalanuvchi: anjir
dastur: Siz tanlagan quyidagi mahsulotlar do'konimizda bor: olma, non, tuz
        Quyidagi mahsulotlar esa do'konimizda yo'q: sut, anjir
        Haridingizdan mamnunmiz ! 

2)
dastur: Assalomu aleykum UITC Academiyasiga hush kelibsiz !")
        Bizning Academiyamizda quyidagi kurslar mavjud: Frontend, Backend, Grafik dizayn, 3D modeling
        Siz qaysi kursni tanlaysiz ?
foydalanuvchi: frontend
dastur: Bizda bunday kurs yo'q iltimos to'gri yozing(agar ro'yhatdagi yo'q kurs kiritilsa)
        Front end ursining narxi 500,000 so'm

3) Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
    -ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
    -GM uchun ikkala harfni katta qiling.
    -Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
    
4) Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini 
    hisoblab konsolga chiqaring. 
    -Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 

5) Parol tizimi. Foydalanuvchidan parol o'rnatishini so'rang. u ikki marta parol kiritsin.
    Kiritiladigan parol eng kamida 8ta belgiga teng bo'lishi kerak.
    Agar ikkala parol bir biriga teng bo'lsa; "Parol fuvaffaqiyatli o'rnatildi" degan
    habar chiqsin. Agar teng bo'lmasa "Xatolik ! Iltimos parolni boshqatdan kiriting"
    degn habar chiqsin.
    -va keyin parolni foydalanuvchidan boshqattan so'rasin, agar foydalanuvchi o'zi kiritgan
    parolni to'g'ri kiritsa, "Hush kelibsiz Admin" desin. Agar parol noto'g'ri kiritilsa
    "Parol xato" degan xabar chiqasin.

6) uchta haqiqiy son berilgan ulardan musbatlarining kubini chiqaradigan dastur tuzing.

"""

""" Javoblar """
""" 1-masala """
# mahsulotlar = ['olma', 'anor', 'non', 'shakar', 'tuz', 'qaymoq']
# yoq = []
# xarid = []
# print("Assalomu aleykum do'konimizga hush kelibsiz !")
# print("Bizda quyidagi mahsulotlar bor:", end=' ')
# for mahsulot in mahsulotlar:
#     print(f"{mahsulot}", end=' ')

# savol = int(input("\nNechata mahsulot sotib olmoqchisiz: "))
# for n in range(savol): # [0,1,2,3,4]
#     meva = input(f"{n+1}-mahsulotni kiriting: ")
#     if meva in mahsulotlar:
#         xarid.append(meva)
#     else:
#         yoq.append(meva) 
                   
# print(f"Bizda yo'q mahsulotlar:", end=" ")
# for y in yoq:
#         print(f"{y}", end=" ")
# print(f"\nBizda bor mahsulotlar: {xarid}")

""" 2-masala """
# print("Assalomu aleykum UITC Academiyasiga hush kelibsiz !")
# print("Bizning Academiyamizda quyidagi kurslar mavjud: \nFrontend \nBackend \nGrafik dizayn \n3D modeling")

# savol = input("Siz qaysi kursni tanlaysiz ?").lower()
# # print(savol)

# if savol == 'frontend':
#     narx = 500_000
#     print(f"{savol.title()} kursining narxi {narx} so'm")
# elif savol == 'grafik dizayn' or savol == '3d modeling':
#     narx = 550_000
#     print(f"{savol.title()} kursining narxi {narx} so'm")
# elif savol == 'backend':
#     narx = 600_000
#     print(f"{savol.title()} kursining narxi {narx} so'm")
# else:
#     xato = "Bizda bunday kurs yo'q iltimos to'gri yozing"
#     print(xato)


""" 3 """
cars=["toyota","mazda","hyundai","gm","kia"]
# for car in cars :
#   if car=="gm"  :
#     print(car.upper())
#   else:
#     print(car.title())

# for car in cars: # != 
#     if car != "gm" :
#         print(car.title())
#     else:
#         print(car.upper())

""" 4 """
# import math

# son = int(input("Son kiriting: "))
# if son > 0:
#     print(f"{son} ning ildizi {round(math.sqrt(son), 3)}")
# else:
#     print("Musbat son kiriting!!!")

""" 5 """
# ha = 0
# print("Assalomu aleykum")
# parol1 = input("Iltimos o'zingiz uchun parol kiriting(parol eng kamida 8 ta belgidan iborat bo'lsin): ")
# parol2 = input("Parolni yana bir bor takrorlang: ")
# if parol1 == parol2 and len(parol1) >= 8:
#     print("Parol muvafaqqiyatli o'rnatildi")
#     ha = 1
# else:
#     if len(parol1) < 8:
#         print("Xatolik ! Eng kamida 8 ta belgi bo'lishi kerak")
#     else:
#         print("Xatolik ! Iltimos parolni boshqatdan kiriting")
# if ha == 1:
#     parol3 = input("Tizim`ga kir`ish uchun parolingizni kiriting: ")
#     if parol1 == parol3:
#         print("Hush kelibsiz Admin")
#     else:
#         print("Parol xato !!!!")

""" 6 """
""" foyadalanuvchi o'zi son kiritssa """
# sonlar = []
# for n in range(3):
#     son = int(input(f"{n+1}- sonni kiriting: "))
#     sonlar.append(son)
# for son in sonlar:
#         if int(son) > 0:
#             print(f"{son} ning kubi {son**3} ga teng ")
        
""" tayyor sonli ro'yhat berilsa """
# sonlar = [3, 5.6 ,-7]
# for son in sonlar:
#     if son > 0 and son == int(son):
#         print(f"{son} ning kubi {son**3} ga teng ")






