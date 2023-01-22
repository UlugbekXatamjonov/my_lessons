"""
Thame: Matnlar(String) bilan ishlash
"""

"""
Vazifa:

1) "" va '' qatnashgan 5 ta turli gaplar tuzing
2) title(), upper(), capitalize(), lower() ni qatnashgan 2 tadan gap yozing(har biriga)
3) strip(), lstrip(), rstrip() qatnashtirib har biri uchun gap yozing
4) input() yordamida foydalanuvchidan oila azolari haqida malumot oling; ismi, familyasi, yoshi, kasbi va boshqalar
 va ularni f"" yordamida mazmunli holatda konsulga chiqaring.
5) len(), replace(), split() larni har birini ishltib turli gaplar yozing.
6) Mahsus belgilar \' \" \n \r \t \b qatnashgan gaplar yozing.

Yuqoridagi gaplarni har birini print() yordamida mazmunli tarzda konsulga chiqarinmg !!!

"""


""" Javoblar """
""" 1 """
# print("Bug'u yugurib uzoqlarga ketdi.")
# print("Bugun hamma yoq judayam \"issib\" ketdi.")
# print('anvar o\'g\'li bilan bog\'chag ketdi.')
# print('Bog\'da o\'rik gulladi.')
# print("G'ordan g'alati ovozlar eshitildi.")

""" 2 """
# ism = 'Ali'
# familya = "Olimov"
# yosh = 23
# mashina = 'Nexia'
# print(f"{ism.title()}ning {mashina}si bor")
# print(f"{familya.title()} bugun majlisga kech keldi.")
# print(f"Maydonda {yosh}ta o'yinchi o'ynayapdi.")
# print(f"Afto halokatda {mashina.upper()} yaroqsiz holatga keldi.")

""" 3 """
# meva1 = "    olma"
# meva2 = "olcha     "
# meva3 = "   nok     "
# print(f"Sevaraning sevimli mevasi {meva1.lstrip()}")
# print(f"Bog'da {meva2.rstrip()}lar g'arb pishibdi.")
# print(f"Kechagi shamolda {meva3.strip()}lar yerni qoplab oldi.")

""" 4 """
# ota_ism = input("Otangizning ismi: ")
# ota_familya = input("Otangizning familyasi: ")
# ota_yosh = input("Otangizning yoshi: ")
# ota_kasbi = input("Otangizning kasbi: ")
# print(f"Otangizning ismi {ota_ism.title()}, familyasi {ota_familya.title()},\
# yoshi {ota_yosh}, kasbi {ota_kasbi.lower()}.")


""" 5 """
# mashina = "Lasetti"
# print(len(mashina))

# py = "I'm backend software engineer and my main lenguage is python"
# print(py.replace('o','a'))

# fruts = "olma, anjir, nok, behi"
# print(fruts.split(','))

""" 6 """
# print('G\'oliblar taqdirlandi.')
# print("Mening \"katta\" kuchugim bor.")
# print("Ko'proq o'z ustingizda \nishlang!")
# print("Mehnat qiling va albatta \rsamarasini ko'rasiz")
# print("Django pyhtonning \tkurubxonasi hisoblanadi.")
# print("Python dunyodagi eng yaxshi  \bdasturlash tili hisoblanadi.")







