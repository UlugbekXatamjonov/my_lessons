"""
Thame: Funkcions(Funksiyalar)
"""

"""
Funksiya - Funksiya ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi.
Biz shu vaqtgacha ko'rib o'tgan funksiyalar: print(), len(), sum(), max(), min()...
"""

""" Funksiya yaratish """
# def salom():
#     print("Assalom aleykum")
# salom()

""" DOCSTRING """
""" 
    DOCSTRING ---> Defenition
    Docstringni konsolga chiqarish uchun print(funksiya_nomi.__doc__) deb ham yozishimiz mumkin: 
"""

def salom_ber(ism):
    """ Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya. ism -> Matn kiritish kerak """
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
salom_ber("Ali")
salom_ber("VAli")
salom_ber('Umar')

"""
    Funksiyaga nom berishda fe'l, ya'ni harakatni bildiruvchi so'zlar yoki jumlalardan foydalaning. 
    Bu bilan siz o'zgaruvchi va funksiya o'rtasini farqlashingiz oson bo'ladi. 
    Misol uchun, yuqorida biz funksiyamizni salom emas salom_ber deb nomladik.
"""

""" Funksiyaga qiymat uzatish """
# def hisobla(tyil, yil):
#     """Foydalanuvchi yoshini hisoblovchi funksiya"""
#     yosh = yil - tyil
#     print(f"Siz {yosh} da ekansiz")
    
# hisobla(2020, 1990)

""" Argumentni kalit so'z bilan uzatish """
# def plus(son1, son2):
#     """ Foydalanuvchi kiritgan sonlarni bir biriga qo'shib beradi. """
#     son3 = son1 + son2
#     print(f"Siz kiritgan {son1} va {son2} larning yig'indisi {son3} ga teng.")
# plus(son2=3,son1=5)

""" Standar qiymat uzatish """
"""
    Funksiya yaratishda, standart qiymatga ega parametrlar doim oxirida yozilishi kerak. 
    Aks holda xatolik yuzaga keladi.
"""     
# def full_name(ism, familya="Olimov"):
#     print(ism, familya)
# full_name("Ali")
# full_name("Asadbek","Mirzanvarov")

# def full_name(familya, ism="Ahmad",):
#     print(ism, familya)
# full_name("Olimov")
# full_name("Alijonov","Jasur")


# def kv(son):
#     """ Kiritilgan sonning kvadratini hisoblovchi funksiya, son - int"""
#     son_kv = son**2
#     print(f"Siz kiritgan {son} ning kvadrati {son_kv} ga teng")
# kv(4)
# kv(5)


"""
Vazifa:

1) Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
2) Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
3) Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
4) Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
    Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
5) Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
6) Foydalanuvchidan uning oila azolari haqidagi malumotlarmni olibn ularni konsulga chiqaruvchi funksiya 
    yozing. M: ismi, yoshi, kasbi...
7) Tog'ri to'rtburchakli uchburchakning katetlarini qabul qilib olib uning gipotenuzsini hisoblovchi funksiya 
    yozing, 2- katetni o'zgarmas parameter sifatida bering.

Yuqoridagi har bir funksiyaga to'liq tarif(defenition yozing)

"""