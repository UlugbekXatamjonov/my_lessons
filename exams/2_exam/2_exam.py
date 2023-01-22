"""
Pythondan 2-imtihon savollari 
Thames: streengs, numbers, if-else-elif, for, lists, dictionary, while
Tests       -> 20
Next step   -> 15+
Good result -> 18+

KEYS = 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
       D C C A D B C A D  A  B  B  D  B  C

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
1) Quida berilgan ro'yhatda  "Albanian" ning indexlari nechi ?
   country = ["Uzbekistan", "Afrikaans", "Albanian", "Russian", "Serbian", "Serbian"]
A) -2, 2       B) 2, -5     C) 3, -4       D) 2, -4

2) Quidagilardan qaybiri to'g'ri ?
A) print('a'lochi')                           B) print("G'ani bugun shapaloqni "kattasini" yedi")
C) print("Lola o'rik tagida o'tiribdi")       D) print('"2-B" sinfi a'\lochilar sinfi')

3) tuple() funksiyasining vazifasi ?
A) O'zgaruvchan ro'yhat yaratish       B) O'zgarmas lug'at taratish
C) O'zgarmas ro'yhat yaratish          D) O'zgaruvchi turini o'zgarmas qilish

4) Matndagi barcha so'zlarning 1-harfini katta qilib beruvchi metod nomi ?
A) title()     B) upper()       C) capitalize()        D) lower()

5) lover() metodining vazifasi ?
A) Matndagi 1-so'zning 1-harfini katta qilib chiqaradi     B) Barcha harflarni kichik qilib chiqaradi
C) Barcha hariflarni katta qilib chiqaradi                 D) Bunday metod yo'q

6) "kichik yoki teng" belgisini to'gri ko'rsating
A) =<      B) <=     C) ==      D) >=<

7) mevalar deb nomlangan lug'atga to'gri element qo'shilgan javobni toping
A) mevalar['bobur'] = anor         B) mevanlar['bobur'] = 'anor'
C) mevalar['bobur'] = 'anor'       D) mevalar[bobur] = 'anor'

8) taomlar lu'g'atidagi 'hasan' keyiga mos keluvchi qiymat to'gri o'zgartirilgan javobni belgilang.
A) taomlar["hasan"] = 'qozon_kabob'        B) taomlar[hasan] = 'qozon_kabob'
C) taonlar["hasan"] = 'qozon_kabob'        D) taomlar["hasan"] = qozon_kabob

9) Lug'atga tegishli metodlar to'gri berilgan javobni toping 
A) key(), value(), item()               B) keys(), append(), values()
C) append(), remove(), insert()         D) keys(), values(), items()

10) insert() metodining vazifasi nima ?
A)  Ro'yhatga elementni indexi bo'yicha qo'shadi       B)  Ro'yhatdan elementni indexi bo'yicha o'chiradi
C)  Ro'yhatdan elementni sug'urib oluvchi metod        D)  Sonli oraliq shakillantirish uchun funksiya

11) Quyidagi funksiyalardan qay biri ro'yhatdan elementni qiymati bo'yicha o'chiradi ?
A) range()     B) remove()      C) delete()        D) del

12) Quidagi lug'atdan 'chinnigul' elementi konsulga to'gri chiqarilgan javobni toping
    qizlar = {
        "anora":['atirgul','lola'],
        "ezoza":['binafsha','moychechak'],
        "dilshoda":['nastarin','chinnigul'],
        "nigina":['kaktus','atirgul']    
    }
A) print(['dilshoda'][0])           B) print(qizlar['dilshoda'][1])
C) print(qizlar['ezoza'][0])        D) print(['dilshoda'][1])

13) Natijani toping.
    sonlar = [1,2,3,4,5,6,7,8,9,10]
    for son in sonlar:
        if son <= 0 and son < 4:
            print(son)
A) 0,1,2,3          B) 1,2,3         C) 5,6,7,8,9,10        D) (hech narsa)

14) Natijani toping.
    sonlar = [1,2,3,4,5,6,7,8,9,10]
    for son in sonlar:
        if son > 0 or  son < 0:
            print(son)
A) 0,1,2,3     B) 1,2,3 ... 7,8,9,10        C) 1,2,3,5,6,7,8,9,10      D) (hech narsa)

15) get() metodining vazifasi
A) ro'yhatdagi yo'q element o'rniga xatolik matnini chiqaradi      B) ro'yhatdagi elementlarni chaqiradi
C) lug'atdagi yo'q element o'rniga xatolik matnini chiqaradi       D) lug'atdagi elementlarni qiymatini chaqiradi

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
while True:
    son = input("Biror son kiriting: ")
    if son.lower() == 'exit' or son.lower() == 'quit':
        print("Dastur tugadi!")
        break
    elif son.isdigit() and int(son) > 0:
        print(f"Siz kiritgan {int(son)} sonining 3-darajasi {int(son)**3} ga va 4-darajasi {int(son)**4} ga teng")
    elif  son.isdigit() and int(son) <= 0:
        continue
    else:
        print("Iltimos musbat son kiriting !!!")
        
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
