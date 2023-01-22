"""
Thame: Ro'yhatlar(Lists)
"""

""" 
Vazifa:

1) ismlar degan ro'yxat yarating va kamida 5 ta yaqin do'stingizning ismini kiriting. 
   Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 

2) sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang(musbat, manfiy, butun, o'nlik). 
    Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. 
    Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa o'chiring. 

3) aktyorlar va honandalar degan ro'yhatlar yarating va ularga o'zingiz eng ko'p kuzatadigan
    aktyorlar va honandalar ni kiriting, ulardan ikkitadan aktyorni o'chirib tashalng, va yangi 3tadan qo'shing.
    song'ra har ikkala ro'yhatdagi elementlarni insonlar degan yangi ro'yhatga jamlang.

4) friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan 
    do'stlaringizni kiriting. Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi 
    yordamida o'chrib tashlang. Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

5) Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() 
    metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends 
    ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

6) O'zingizga ma'lum davlatlarning ro'yxatini tuzing(eng kamida 10 ta) va ro'yxatni konsolga chiqaring.
    -ro'yxatning uzunligini konsolga chiqaring;
    -sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring;
    -sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring;
    -asl ro'yxatni qaytadan konsolga chiqaring;
    -reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring;
    -sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring;

7) 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
    -ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring;
    -ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring;
    -ro'yxatdagi elementlar sonini hisoblang;
    -ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring;

8) Taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting.
    -nonushta degan yangi ro'yxatga taomlardan nusxa oling;
    -yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing;
    -ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring;
""" 


""" Javoblar """

""" 1 """
# ismlar = ["Ali", "Ibrohim", "dilshodbek", "Azizjon", "Zafarbek", "Zuhriddin"]
# print(f"Salom {ismlar[0]}. Axvollaring yaxshimi")
# print(f"Men bugun do'stim {ismlar[1]} bilan birgalikda futbol o'ynadim.")
# print(f"Mening {ismlar[2]} degan do'stim g'irt ikkichi, u doim 2 oladi :)")
# print(f"{ismlar[3]} bugun do'stlariga judayam katta yordam ko'rsatdi.")
# print(f"Daraxt ostida uxlab yotgan {ismlar[-2]} ning boshiga olma tushdi.")
# print(f"{ismlar[-1]} va {ismlar[-3]} qaln do'stlar")

""" 2 """
# sonlar = [3,7,-5,123,-64,0,45.3,-76.4,43,12,66,-87]
# print(sonlar[0]+sonlar[1]+sonlar[2]+sonlar[3])
# print(sonlar[-5]/sonlar[1]*sonlar[-2])
# sonlar[2] = 5
# sonlar[-5] = 33
# sonlar[6] = -98
# sonlar.remove(7)
# sonlar.remove(43)
# sonlar.remove(-87)
# del sonlar[-5]
# print(sonlar)


""" 3 """
# aktyorlar = ["Jony Deep", "Ulug'bek Qodirov", "Wil Smith"]
# honandalar = ["Alan Walker", "Dabro", "Mband", "Ulug'bek Rahmatullayev"]
# print(aktyorlar, honandalar)
# del aktyorlar[2]
# del honandalar[2]
# print(aktyorlar, honandalar)
# aktyorlar.append("Morgan")
# aktyorlar.append("Harry Potter")
# honandalar.append("One Direction")
# print(aktyorlar, honandalar)

# insonlar = []
# insonlar.extend(aktyorlar)
# insonlar.extend(honandalar)
# print(insonlar, honandalar, aktyorlar)

""" 4 """
# friends=[]
# friends.append("Asadbek")
# friends.append("Ilg'or")
# friends.append("Mirazim")
# friends.append("Nursaid")
# print(friends)

# friends.remove("Ilg'or")
# print(friends)

# friends.append("Javohir")
# friends.append("Hojiakbar")
# friends.insert(2,"Sunnatali")
# friends.insert(6,"Dilshodbek")
# print(friends)

""" 5 """
# mehmonlar=[]
# mehmonlar.append(friends.pop(2))
# mehmonlar.append(friends.pop(-1))
# print(mehmonlar)


# O'zingizga ma'lum davlatlarning ro'yhatini tuzing va uni konsulga chiqaring 
# davlatlar=("Daniya" ,"Angilya","Malayzia","Shvetsia","Rossia" ) 
# print(davlatlar)

#2
# Ro'yhatning uzunligini konsulga chiqaring
# print(len(davlatlar))

#3
# sorted() funksiasi yordamida ro'yhatni tartiblangan holatda konsulga chiqaring
# print(sorted(davlatlar)) 

#4
# sorted() yordamida ro'yhatni teskari ko'rinishda konsulga chiqaring
# print(sorted(davlatlar , reverse=True))

#5
# 120 dan 1200 gacha bo'lgan juft sonlar ro'yhatini tuzing
# sonlar=list(range(120,1200,2))
# print(sonlar)

#6
# Ro'yhatdagi sonlar yig'indisini toping va uni konsulga chiqaring
# print(sum(sonlar))
# 
#7
# Ro'yhatdagi eng katta va eng kichik son o'rtasidagi ayrmani hisoblang va konsulga chiqaring
# print(max(sonlar) - min(sonlar)) 

#8
# Ro'yhatdagi elementlar sonini konsulga chiqaring
# print(len(sonlar))

#9
# Ro'yhatning boshidan , o'rtasidan , oxiridan 20 ta elementni konsulga chiqaring

# print(sonlar[:20])
# print(sonlar[260:280])
# print(sonlar[520:])

#10
# taomlar degan ro'yhat yarating va ichiga 5 ta taomni kiriting
# taomlar=("Osh","shashlik","manti","sho'rva","bog'irsoq")
# print(taomlar)

#11
# nonushta degan yangi ro'yhatga taomlardan nusha olig
# nonushta=[]
# nonushta=taomlar[:]
# nonushta = list(nonushta)
# print(nonushta)

#12
# yangi ro'yhatda faqat nonushtada yeyiladigan taomlar qoldiring va yangi 2 ta taom qo'shing

# nonushta.remove("Osh")
# nonushta.remove("shashlik")
# nonushta.remove("manti")
# nonushta.remove("sho'rva")
# print(nonushta)

# nonushta.append("qaymoq")
# nonushta.append("Asal")
# nonushta.insert(1, "Sut")
# print(nonushta)


















