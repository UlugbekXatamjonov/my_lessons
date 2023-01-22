"""
Thame: Funkcions(Funksiyalar)
"""

""" Javoblar """

""" 
1) Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va 
    telefon raqamini qabul qilib, lug'at ko'rinishida malumot qaytaruvchi funksiya yozing. 
    Lug'atda foydalanuvchi yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy 
    qiling (masalan, tel.raqam, el.manzil)
"""
# def mijiz_info(ism,familya,tjoy,tyil,tel=" ",gmail=" ") :
#     """Mijoz haqidagi ma'lumotlarni shakllantiruvchi funksia"""
#     mijoz = {'ism': ism,
#               'familya':familya,
#               'tyoy': tjoy,
#               'yoshi': 2021-tyil,
#               "tel":tel,
#               "gmail": gmail,}
#     return mijoz
# mijoz1 = mijoz_info("Umarbek", "Mansuraliyev", "Namangan", 2001, "+998911777901")
# mijoz2 = mijoz_info("Sarvarbek", "Abdullayev", "Navoiy", 1999, gmail="sarvar99@gmail.com")
# mijozlar = [mijoz1, mijoz2]

# print("Mijozlar: ")
# for mijoz in mijozlar :
#     print(f"{mijoz['ism'].title()} {mijoz['familya'].title()}",
#           f"{mijoz['yoshi']} yoshda , telefon raqami {mijoz['tel']}")



""" 2) Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan 
    ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
"""
# def mijiz_info(ism,familya,tjoy,tyil,tel=" ",gmail=" ") :
#     """Mijoz haqidagi ma'lumotlarni shakllantiruvchi funksia"""
#     mijoz = {'ism': ism,
#               'familya':familya,
#               'tyoy': tjoy,
#               'yoshi': 2021-tyil,
#               "tel":tel,
#               "gmail": gmail,}
#     return mijoz

# print("Mijoz haqidagi malumotlarni kiriting: ")
# mijozlar = []

# while True:
#     ism = input("Ismi: ")
#     familya = input("Familyasi: ")
#     tjoy = input("Tug'ilgan joyi': ")
#     tyil= int(input("Tug'ilgan yili: "))
#     tel = input("Telefon raqami: ")
#     gmail = input("Gmailli: ")
    
#     mijozlar.append(mijiz_info(ism,familya,tjoy,tyil,tel,gmail))
#     savol = input("Davom etasizmi(yes/no)? ")
#     if savol.lower() != "yes" :
#         break
    
# print("Mijozlar: ")
# for mijoz in mijozlar :
#     print(f"{mijoz['ism'].title()} {mijoz['familya'].title()}",
#           f"{mijoz['yoshi']} yoshda , telefon raqami {mijoz['tel']}")
    


""" 3) Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
"""
# def kattasi(x,y,z):
#     if y>=x:
#         x = y
#     if z>=x:
#         x = z
#     return x

# a = kattasi(1,2,4)
# print(a)



""" 4) Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, 
    perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
"""
# def aylana_info(radius,p=3.14):
#     aylana = {"radius":radius,
#               "diametr":radius*2,
#               "perimetr":p*radius*2,
#               "yuza":p*radius**2}
#     return aylana
# a1 = aylana_info(5)
# a2 = aylana_info(7)
# print(a1)
# print(a2)



""" 5) Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya 
    yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan 
    katta musbat sonlar)
"""
# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar

# a1 = tub_sonlar_top(1,100)
# print(a1)

""" 6) Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi 
    sonlar ro'yxatni qaytaruvchi funksiya yozing.  
    Ta'rif: Har bir hadi o'zidan oldingi ikkita hadning yig'indisiga teng bo'lgan 
    ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang'fzish had ko'pincha 
    1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
"""
# def fibonaci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar


# a1 = fibonaci(10)
# print(a1)




