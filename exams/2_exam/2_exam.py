"""
Pythondan 2-imtihon savollari 
Thames: Dictionary, while, Functions, try-exept, 
Tests       -> 20
Next step   -> 15+
Good result -> 18+

KEYS = 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
       C D A B D A C A D  A  C  B  A  B  C

16)
while True:
    son = input("Biror son kiriting: ")
    if son.lower() == 'exit' or son.lower() == 'quit':
        print("Dastur tugadi!")
        break
    elif int(son) > 0:
        print(f"Siz kiritgan {int(son)} sonining 3-darajasi {int(son)**3} ga va 4-darajasi {int(son)**4} ga teng")
    elif int(son) <= 0:
        continue
        
17)
insonlar = {
    "inson" : {
        "ism":"ALi",
        "familya":'Valiyev',
        "t_yil":2000,
        "kasbi":"o'qtuvchi"    
    },
}
print(f"{insonlar['inson']['ism']} {insonlar['inson']['familya']} {insonlar['inson']['t_yil']}-yili tug'ilgan, kasbi {insonlar['inson']['kasbi']}")

18)
x = 1
while x < 10:
    print(x)
    x = x + 1


19)
son = int(input("Istalgan son kiriting: "))
if son > 0:
    print(f"{son} musbat")
elif son == 0:
    print(f"{son} 0 ga teng")
else: 
    print(f"{son} manfiy")


20)
taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':"lag'mon",
}
print(taomlar.get("abror","Bunday key yo'q"))

"""

"""
1) Quidagi variantlardan qaybirida abadiy tsikil mavjud ?
A) While True:   B) while False:  C) while True: D) while true:
       pass             pass             pass           pass
2) Abadiy tsiklni to'xtatuvchi operator ko'rsatilgan javobni belgilang
A) Break    B) continue    C) while   D) break

3) Funksiya yaratish kalit so'zi ?
A) def      B) class     C) return        D) break

4) "Docstring" nima ?
A) Izoh     B) Funksiya haqida ma'lumot beruvchi matn  
C) Funksiya nomi   D) Oddiy matn
 
5) lover() metodining vazifasi ?
A) Matndagi 1-so'zning 1-harfini katta qilib chiqaradi     B) Barcha harflarni kichik qilib chiqaradi
C) Barcha hariflarni katta qilib chiqaradi                 D) Bunday metod yo'q

6) Funksiyadan qiymat qaytarish uchun qaysi kalit so'zdan foydalanamiz ? 
A) return   B) pass    C) break     D) Return

7) mevalar deb nomlangan lug'atga to'gri element qo'shilgan javobni toping
A) mevalar['bobur'] = anor         B) mevanlar['bobur'] = 'anor'
C) mevalar['bobur'] = 'anor'       D) mevalar[bobur] = 'anor'

8) taomlar lu'g'atidagi 'hasan' keyiga mos keluvchi qiymat to'gri o'zgartirilgan javobni belgilang.
A) taomlar["hasan"] = 'qozon_kabob'        B) taomlar[hasan] = 'qozon_kabob'
C) taonlar["hasan"] = 'qozon_kabob'        D) taomlar["hasan"] = qozon_kabob

9) Lug'atga tegishli metodlar to'gri berilgan javobni toping 
A) key(), value(), item()               B) keys(), append(), values()
C) append(), remove(), insert()         D) keys(), values(), items()

10) Uzatilayotgan argumentlar soni nomalum bo'lsa biz qaysi usuldan foydalanamiz ?
A) *args    B) args  C) **kwargs    D) key = argument 

11) Uzatilayotgan "kalit so'z - qiymat" ko'rinishidagi argumentlar soni nomalum bo'lsa 
    biz qaysi usuldan foydalanamiz ?
A) *args    B) kwarg  C) **kwargs    D) kwargs

12) Quidagi lug'atdan 'chinnigul' elementi konsulga to'gri chiqarilgan javobni toping
    qizlar = {
        "anora":['atirgul','lola'],
        "ezoza":['binafsha','moychechak'],
        "dilshoda":['nastarin','chinnigul'],
        "nigina":['kaktus','atirgul']    
    }
A) print(['dilshoda'][0])           B) print(qizlar['dilshoda'][1])
C) print(qizlar['ezoza'][0])        D) print(['dilshoda'][1])

13) Quidagilardan qaysi biri sizga xatolarni tekshirishga imkon beradi ?
A) try B) else  C) raise D) except

14) Xech qanday xatolik yuzaga kelmagan xollarda quidagilardan qay biri ishga tushadi ?
A) try   B) else    C) raise    D) except

15) get() metodining vazifasi
A) ro'yhatdagi yo'q element o'rniga xatolik matnini chiqaradi      
B) ro'yhatdagi elementlarni chaqiradi
C) lug'atdagi yo'q element o'rniga xatolik matnini chiqaradi       
D) lug'atdagi elementlarni qiymatini chaqiradi

16) Foydalanuvchi kiritgan sonlardan faqat musbatlarini 3 va 4 chi darajasini qaytaruvchi dastur tuzing.
    Agar foydalanuvchi manfiy yoki 0 kiritsa dastur ishlashda davom etsin. 'exit', 'quuit' deb yozgandagina
    dastur to'xtasin. 

17) Quidagi lug'atdagi qiymatlarni konsulga mazmunli holatda chiqaring(for() operatori siz).
insonlar = {
    "inson" : {
        "ism":"ALi",
        "familya":'Valiyev',
        "t_yil":2000,
        "kasbi":"o'qtuvchi"    
    },
}

18) Quidagi abadiy tsiklni, abadiylikdan chiqaring.
x = 1
while x < 10:
    print(x)

19) Foydalanuvchi kiritgan istalgan sonning manfiy, musbat yoki uning 0 teng ekenligini qaytaring

20) Quida berilgan lug'atda mavjud bo'lmagan 'abror' keyi uchun get() metodini to'gri qo'llang
taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':"lag'mon",
}

"""

# 16)
# while True:
#     son = input("Biror son kiriting: ")
#     if son.lower() == 'exit' or son.lower() == 'quit':
#         print("Dastur tugadi!")
#         break
#     elif son.isdigit() and int(son) > 0:
#         print(f"Siz kiritgan {int(son)} sonining 3-darajasi {int(son)**3} ga va 4-darajasi {int(son)**4} ga teng")
#     elif  son.isdigit() and int(son) <= 0:
#         continue
#     else:
#         print("Iltimos musbat son kiriting !!!")
        
# 17)
# insonlar = {
#     "inson" : {
#         "ism":"ALi",
#         "familya":'Valiyev',
#         "t_yil":2000,
#         "kasbi":"o'qtuvchi"    
#     },
# }
# print(f"{insonlar['inson']['ism']} {insonlar['inson']['familya']} {insonlar['inson']['t_yil']}-yili tug'ilgan, kasbi {insonlar['inson']['kasbi']}")

# 18)
# x = 1
# while x < 10:
#     print(x)
#     x = x + 1


# 19)
# son = int(input("Istalgan son kiriting: "))
# if son > 0:
#     print(f"{son} musbat")
# elif son == 0:
#     print(f"{son} 0 ga teng")
# else: 
#     print(f"{son} manfiy")


# 20)
# taomlar = {
#     'ali':'osh',
#     'vali':'shashlik',
#     'hasan':"lag'mon",
# }
# print(taomlar.get("abror","Bunday key yo'q"))
