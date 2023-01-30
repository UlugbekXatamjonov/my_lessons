"""
Thame: Funkcions(Funksiyalar)
"""
"""
Vazifa:

1) Avvalgi darslarimizda bajargan parol tizimi haqidagi dasturimizni 'password.py' fayliga qayta yozing.
    Va uni yangi 'main.py' fayliga chaqirib olib ishlating.

2) Inson haqidagi malumotlarni qabul qilib olib, ularni lug'at ko'rinishida qaytaradigan funksiyani 
    'person.py' fayliga yozing. va uni ham 'main.py' fayliga chaqirib olib ishlating. Funksiya yozishda *args va *kvargs
    usullaridan foydalaning.

"""

""" Javoblar """

from password import password_func
from person import person_info

""" 1 """
# password_func()

""" 2 """
person1 = person_info("Umarbek", "Mansuraliyev", "Namangan", 2001, "+998911777901")
person2 = person_info("Sarvarbek", "Abdullayev", "Navoiy", 1999, gmail="sarvar99@gmail.com")
persons = [person1, person2]

print("Insonlar: ")
for person in persons :
    print(f"{person['ism'].title()} {person['familya'].title()}",
          f"{person['yoshi']} yoshda , telefon raqami {person['tel']}")
    
    
    