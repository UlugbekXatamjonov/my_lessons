"""
Pythondan 1-imtihon savollari 
Thames: streengs, numbers, for, lists, tuple, if-else-elif, boolen, operators
Tests       -> 30   
Next step   -> 22+
Good result -> 28+

KEYS = 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
       A C B A D C C A C A  B  C  D  B  B  A  C  D  B  A  D  B  C  A  B
       
26) print(ism +' '+ familya , yosh , "yoshda")

27) sonlar = range(9,45,2)
        # print(sonlar)
 
28)
tyil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh = 2023-tyil
print(f"Siz {yosh} yoshda siz")

29)
ismlar = ["Ali", "Olim", "Hasan", "Husan", "Vali"]
ismlar.remove("Ali")
ismlar.remove("Olim")
ismlar.append("Tolib")
ismlar[1] = "Husan Hasanov"
print(ismlar)

30)
sonlar = list(range(20,31))
for son in sonlar:
    print(f"{son} ning 4-darajasi {son**4} ga teng")
"""

"""
<--  Savollar  -->

1) O'zgaruvchining turini aniqlab beruvchi funskiya nomi ?
A) type()
B) str()
C) float()
D) len()

2) Quidagilardan qaybiri to'g'ri ?
A) print('a'lochi') 
B) print("G'ani bugun shapaloqni "kattasini" yedi")
C) print("Lola o'rik tagida o'tiribdi")
D) print('"2-B" sinfi a'\lochilar sinfi')

3) Matndagi barcha harflarni katta qilib beruvchi metod nomi ?
A) title()
B) upper()
C) capitalize()
D) lower()

4) Matndagi barcha so'zlarning 1-harfini katta qilib beruvchi metod nomi ?
A) title()
B) upper()
C) capitalize()
D) lower()

5) lover() metodining vazifasi ?
A) Matndagi 1-so'zning 1-harfini katta qilib chiqaradi
B) Barcha harflarni kichik qilib chiqaradi
C) Barcha hariflarni katta qilib chiqaradi
D) Bunday metod yo'q

6) Sonni ildizdan chiqaruvchi funksiya nomi ?
A) str()
B) int()
C) sqrt()
D) float()

7) 5 ning 7 darajasi ?
A) 5*7
B) 7**5
C) 5**7
D) 5/*5

8) Natijani hisoblang.
    a,b,c = 4,7,-3
    natija = a+(c-(b+a)+b*c)/b
    print(natija)
A) -1.0
B) 5.3
C) 6
D) 0

9) Ro'yhatga element qo'shadigan metod nomi ?
A) list()
B) lower() 
C) append()
D) sorted()

10) insert() metodining vazifasi nima ?
A)  Ro'yhatga elementni indexi bo'yicha qo'shadi
B)  Ro'yhatdan elementni indexi bo'yicha o'chiradi
C)  Ro'yhatdan elementni sug'urib oluvchi metod
D)  Sonli oraliq shakillantirish uchun funksiya

11) Quyidagi funksiyalardan qay biri ro'yhatdan elementni qiymati bo'yicha o'chiradi ?
A) range()
B) remove()
C) delete()
D) del

12) Quyidagi funksiyalardan qay biri ro'yhatdan elementni sug'urib oluvchi metod hisoblanadi ?
A) remove()
B) append()
C) pop()
D) len()

13) Natijani toping.
    sonlar = [1,2,3,4,5,6,7,8,9,10]
    for son in sonlar:
        if son <= 0 and son < 4:
            print(son)
A) 0,1,2,3
B) 1,2,3
C) 5,6,7,8,9,10
D) (hech narsa)

14) Natijani toping.
    sonlar = [1,2,3,4,5,6,7,8,9,10]
    for son in sonlar:
        if son > 0 or  son < 0:
            print(son)
A) 0,1,2,3
B) 1,2,3 ... 7,8,9,10
C) 1,2,3,5,6,7,8,9,10
D) (hech narsa)

15) Takrorlanuvchi operator(funksiya) nomi ?
A) if
B) for
C) elif
D) in

16) replace() metodining vazifasi ?
A) Bir belgini ikkinchisiga almashtirib berish
B) elementni o'chirish
C) ro'yhatdagi elementni boshqasi bilan almashtirish
D) ro'yhatdan elementni sug'urish

17) Matndagi bo'shliqlarni yo'q qilib beruvchi metod  nomi ?
A) lstrip()
B) rstrip()
C) strip()
D) len()

18) O'nlik sonni yaxlidlab beruvchi metod nomi ?
A) rount()
B) math()
C) sqrt()
D) round()

19) Ro'yhatni boshi va oxirini aylantirib beruvchi metod nomi ?
A) sorted(reverse=True)
B) reverse()
C) sort(reverse=True)
D) list()

20) Agar ..... orqali elementni o'chirsak ,  element ro'yhatda bo'lsa o'chiriladi, 
    agar u ro'yhatda bo'lmasa xatolik kelib chiqmaydi.
A) discard()
B) del
C) discart()
D) remove()

21) Ikkita set ni qo'shib,  3-yangi set ni yararuvchi metod nomi ?
A) list()
B) set()
C) update()
D) union()

22) bool() funksiyasining vazifasi ?
A) Mantiqiy qiymat yaratadi
B) Har qanday qiymatni baholashga imkon beradi va bizga True yoki False javobini qaytaradi
C) Taqqoslash operatorlari
D) Mantiqiy qiymat operatori

23) Yaxlidlab bo'lish operatorini belgilang.
A) /
B) =/
C) //
D) /=

24) Azolik operatori to'g'ri ko'rsatilgan javobni tanlang.
A) in / not in
B) or
C) is / is not
D) and

25) Identifikatsiya operatorlari to'g'ri ko'rsatilgan javobni tanlang.
A) in / in not
B) is / is not
C) in / not in
D) and / or / not

26) Quidagi kodagi hatolik(lar)ni aniqlang va kodni xatoliksiz to'g'ri yozing.
ism = 'Abbos'
familya = "Bahromov"
yosh = 20
print(ism +' '+ familya2 + yosh + "yoshda")

27) sonlar deb nomlangan 9 dan 45 gacha toq sonlardan iborat sonli ro'yhat yarating(45 kirmaydi).

28) Foydalanuvchidan uning tug'ilgan yilini kiritishini so'rab, unga yoshini hisoblab beruvchi 
    dastur tuzing.

29) Ismlar deb nomlangan ro'yhat(list) tuzing, unda 5 ta ism bo'lsin.
    Keyin undan 2 ta isimni o'chirib tashlang, 1 ta qo'shing, va 1 ta ismning qiymatini o'zgartiring.

30) 20 dan 30 gacha(30 ham) bo'lgan sonlarning to'rtinchi darajasini hisoblab konsulga chiqaradigan dastur tuzing.

"""
