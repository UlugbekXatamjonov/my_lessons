"""
Thame: While tsikli
"""

"""  Javoblar """

""" 1 
Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
    Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating.
"""
# kitoblar = []
# while True:
#     kitob = input("Sevimli kitobingizni nomini kiriting: ")
#     if kitob.lower() == "exit":
#         break
#     else:
#         kitoblar.append(kitob)
        
# print("Sizning sevimli kitoblaringiz: ")
# for kitob in kitoblar:
#     if kitob == kitoblar[-1]:
#         print(f"{kitob.capitalize()}", end=".")
#     else:
#         print(f"{ kitob.capitalize()}", end=", ")
    
""" 2 
Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va 
chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur 
to'xtasin (ikkita shartni ham tekshiring). Yuqoridagi dasturni turli usullarda
yozib ko'ring (break, ishora)
"""
# print("Assalt bomu aleykum \"Zoo\" hayvonbog'iga hush kelibsiz ")
# ishora = 1
# while ishora:
#     yosh  = input("ILtimos yoshingizni kiriting: ")
#     if yosh.lower() == 'exit' or yosh.lower() == 'quit':
#         print("Bizni hayvonot bog'imizni tanlaganingiz uchun rahmat !")
#         ishora = 0
#     elif yosh.isdigit() and int(yosh) >= 0 and int(yosh) <= 100:
#         if  int(yosh) <=7:
#             narx = 2_000
#         elif int(yosh) <=18:
#             narx = 3_000
#         elif int(yosh) <=65:
#             narx = 7_000
#         elif 65 <= int(yosh) :
#             narx = "bepul"
#         if narx == 'bepul':
#             print(f"Sizga kirish {narx}")
#         else:
#             print(f"Sizga kirish {narx} so'm")
#     elif yosh.isdigit() and int(yosh) >100:
#         print("Iltimos 100 dan kichik son kiriting !")
#     else:
#         print("Iltimos musbat son kiriting")


""" 3 
Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
"""
# print("Kiritilgan sonning ildizini qaytaruvchi dastur.")
# savol = "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input("Musbat son kiriting dasturni to'xtatish uchun 'exit' deb yozing): ")
#     if qiymat.lower() == 'exit':
#         break
#     elif qiymat.isdigit() and int(qiymat) <=0:
#         continue
#     elif qiymat.isdigit():
#         ildiz = round(float(qiymat)**(0.5),3)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
#     else:
#         continue

""" 4 
Foydalanuvchidan tizimga kirishi uchun parol so'rang, foydalanuvchi to'gri javob 
kiritsa unga 'hush keib siz' degan habar chiqsin va dastur to'xtasin. 
Agar foydalanuvchi 3 marta xato parol kiritsa uni abadiy tsiklga tushurib qo'ying.  
"""
# ishora = 1
# while ishora:
#     parol1 = input("O'zingiz uchun parol kiriting: ")
#     parol2 = input("Parolni takrorlang: ")
#     if parol1 == parol2:
#         print("Parol muvaffaqiyatli o'rnatildi\n Hush kelibsiz!")
#         n = 1 
#         while True:
#             savol = input("Iltimos tizimga kirish uchun parolingizni kiriting: ")
#             if savol == parol1:
#                 print("Hush kelibsiz!")
#                 ishora = 0
#                 break
#             elif n == 3:
#                 while True:
#                     print("PAROL XATO!!!!!!!!!!!")
#             elif savol != parol1:
#                 print("Parol xato !!! \nQaytadan urinib ko'ring")
#                 n = n+1
#     else:
#         print("Siz parolni noto'gri takrorladingiz. Iltimos boshqatdan urinib ko'ring")

""" 5 
Online bozor loyihasini qiling. Avvaliga foydalanuvchiga do'koningizdagi mahsulotlarni nomi va narxini ko'rsating,
song foydalanuvchidan nima olishini so'rang, keyin xaridni davom etirasizmi yoki yo'q deb so'rang
agar ha desa yana mahsulot nomini so'rang, agar yoq dasa jarayoni tugatib, sotib olgan mahsulotlari va 
ularning narxini ko'rsating. 
"""
# mahsulotlar = {
#     'olma':5000,
#     "nok":7000,
#     "anor":12000,
#     'banan':13000
# }

# savad = []
# summa = 0

# print("Do'konimizda quyidagi mahsulotlar bor: ")
# for meva, narx in mahsulotlar.items():
#     print(f"{meva} - {narx} so'm")

# while True:
#     meva = input("Sotib olmoqchi bo'lgan mahsulotingiz nomini kiriting:").lower()
#     if meva in mahsulotlar:
#         while True:
#             soni = input("Necha kg sotib olasiz: ")
#             if soni.isdigit() and int(soni) > 0:
#                 savad.append(meva)
#                 for key, value in mahsulotlar.items():
#                     if key == meva:
#                         summa = summa + value * int(soni)
#                 break
#             else:
#                 print("Siz son kiritmadingiz!!!")
#     else:
#         print(f"Kechirasiz do'konimizda {meva} yo'q")
    
#     savol = input("Yana biror nima sotib olasizmi(yes/no): ")
#     if savol.lower() == "yes":
#         continue
#     elif savol.lower() == "no":
#         break
    
# print("Siz quidagi mahsulotlarni sotib oldingiz: ", end=" ")
# for meva in savad:
#     if meva == savad[-1]:
#         print(f"{meva}", end=".")
#     else:
#         print(f"{meva}", end=", ")
# print(f"\nUmmumiy narx: {summa} so'm")

""" 6 
1 dan 100 gacha bo'lgan toq sonlar yig'indisini toping.
"""
# son = 1
# yigindi = 0
# while son < 1000:
#     yigindi = yigindi + son
#     son = son + 2
# print(yigindi)


