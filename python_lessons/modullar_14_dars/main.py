"""
Thame: Funkcions(Funksiyalar)
"""

""" Funksiyaga ro'yhat uzatish """
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)


""" Moslashuvchan funksiya """
"""
Agar funksiyangiz bir nechta argument qabul qilishi kerak bo'lsa-yu, lekin siz argumentlar 
sonini aniq bilmasangiz, Pythonda istalgancha qiymat qabul qiluvchi funksiya yaratish 
imkoniyati bor. 
"""

""" *args usuli """ #   *args ---> arguments
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1,2,3,4,5,6,7,8,9))
# print(summa(-7,0,8))
# print(summa(23))

"""
*args usulida, bacha uzatilgan parametrlar (bir dona bo'lsa ham) funksiya ichida.
o'zgarmas ro'yxatga (tuple) joylanadi.

Agar funksiya bir nechta argument qabul qilsa, *args argument doim oxirida yoziladi.
"""

# def summa(x,y,*sonlar): # funksiyamiz kamida 2 ta parametr qabul qiladi(x va y)
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     a = x+y+sum(sonlar)
#     return a

# print(summa(4, 5, 7, 9))


""" **kwargs usuli """ #  **kwargs ---> keyword arguments(kalit so'zli argumentlar)
"""
Agar funksiyaga kalit so'z - qiymat ko'rinishidagi argumentlarni uzatish talab qilinsa,
va bunday parametrlar soni noma'lum bo'lsa, argument oldidan ikkita yulduzcha qo'yiladi (**kwargs).
"""
# def info(ism, familya, **malumotlar):
#     """ Inson haqidagi malumotlarni lug'at ko'rinishida qaytaradigan funksiya """
#     malumotlar['ism'] = ism
#     malumotlar['familya'] = familya
#     return malumotlar

# inson1 = info("Abubakir", "Olimov")
# inson2 = info("Hasan", "Abdullayev", yosh=34, kasb="haydovchi")
# print(inson1)
# print(inson2)

""" Modullar """
"""
Funksiyaning qulayliklaridan biri, ko'p takrorlanadigan kodlarni funksiya ichida yashirishimiz va 
kerak bo'lgan murojat qilishimiz mumkinligida. Maqsadimiz dasturimizni ixcham va tushunarli qilib, 
kelajakda o'zimiz yoki boshqalar uchun ham "toza" kod qoldrisih. Bu yo'nalishda yana bir qadam qo'yib, 
dasturimizni modullarga ajratimshimiz mumkin. 

Modul bu loyihamiz ichidagi alohida fayl bo'lib, dasturimiz davomida ishlatiladigan funskyalarni 
(va o'zgaruvchilarni) mana shu faylga joylab, ko'zdan yashirib qo'yishimiz mumkin. Bu bizga asosiy 
dasturimizdan chalg'imasdan kod yozish imkoniyatini beradi. 

Modul va uning ichidagi funksiyalarni istalgan payt asosiy dasturimizga yuklab olishimiz, modullarni 
boshqa dasturchilar bilan ulashishimiz yoki kelajakda o'zimizning boshqa loyihalarimizda foydalanishimiz mumkin.
Umuman olganda katta dasturlar bir nech o'nlab modullardan iborat bo'lishi tabiiy hol.

Modul yaratish uchun asosiy dasturimizdagi funksiyalarni yangi faylga ko'chiramiz xolos. 
Modulga oson murojat qilishimiz uchun, bugungi darsimiz uchun bitta "papka"(modullar_darsi) yaratib olamiz va
uning ichida main.py va funksiyalar.py deb nomlangan 2ta papka hosil qilamiz.

"""

""" funksiyalar faylidan kerakli funksiyalarni chaqirib(yuklab) olamiz"""
from funksiyalar import bahola 
from yordamchi_funksiyalar.y_funksiyalar import summa
# from yordamchi_funksiyalar.y_funksiyalar import summa as yigindi

""" bahola() """
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)


""" summa() """
# print(summa(1,2,3,4,5,6,7,8,9))
# print(summa(-7,0,8))
# print(summa(23))


""" as - modul nomini o'zgartirish """
# print(yigindi(1,2,3,4,5,6,7,8,9))
# print(yigindi(-7,0,8))
# print(yigindi(23))







