"""
Thame: Dictionary(Lug'at)
"""

""" Javoblar """

""" 1 
Otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta 
    m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida 
    konsolga chiqaring Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
"""
# otam= {"ism":"ilxomjon", "tyil":1977 , "viloyat":"namangan" }
# ism= otam["ism"]
# tyil= otam["tyil"] 
# vil= otam["viloyat"] 
# print(f"Otamning ismi {ism.title()} , {tyil}-yilda {vil.title()} viloyatida tug'ilgan.")

# onam= {"ism":"nasiba", "tyil":1979, "viloyat":"namangan"}
# ism= onam["ism"]
# tyil= onam["tyil"]
# vil= onam["viloyat"]
# print(f"Onamning ismi {ism.title()} , {tyil}-yilda  {vil.title()} viloyatida tug'ilgan ")


""" 2 
Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
    Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
"""
# taomlar= {"otam":"osh","onam":"mastava","ukam":"shashlik", "men":"manti", "singlim":"dimlama"}
# taom= taomlar["otam"]
# print(f"Otamning sevimli taomi {taom.title()}.")

# taom= taomlar["onam"]
# print(f"Onamning sevimli taomi {taom.title()}.")

# taom= taomlar["ukam"]
# print(f"Ukamning sevimli taomi {taomlar['ukam'].title()}.")


""" 3 
Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z(atamani) kiriting 
    (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
"""
python_lugati ={
    "print":"konsulga yozilgan dasturni chiqarib berdi.",
    "if":"agar deb tarchima qilinadi va birinchi shartni bajaradi",
    "else":"yoki deb tarchima qilinadi va qolgan shartni bajaradi",
    "elif":"ikinchi va boshqa shartlarni bajaradi",
    ".title":"Bu metod berilgan so'zni birinchi harfini konsulga katta qilib berib chiqaradi.",
    ".upper":"Bu metod berilgan so'zni konsulga bacha harflarini katta qilib berib chiqaradi.",
}
# print(python_lugati["print"])

""" 4 
Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
    Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
"""
# eng_uz = {
#     "apple":"olma",
#     "pear":"nok",
#     "peanapple":"ananas",
#     "fig":"anjir",
#     "stawberry":"qulupnay",
#     "greip":"uzum"
# }

# soz = input("Biror meva nomini kiriting: ").lower()
# if eng_uz != soz :
#     print(eng_uz.get(soz, "Bunday so'z mavjud emas."))
# else :
#     print(f"{soz} - {eng_uz}")
    

""" 6 
Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va 
    qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
"""
# pyhton_izohli_lugati = {
#     "print":"matnni konsulga chiqaradi",
#     ".upper":"matnni katta harif bn chiqaradi",
#     ".title":"birinchi harfni katta qilib beradi",
#     "if":"agar",
#     "elif":"agar, yoki",
#     "else":"yoki",
#     "float()":"o'nlik son",
#     "int()":"butun son",
#     "input":"malumot qabul qilai",
# }

# for k , v in sorted(pyhton_izohli_lugati.items()) :
    # print(f"{k}-{v}")


""" 7 
Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni 
    alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
"""
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}

# print('Dunyo davlatlari:')
# for davlat in sorted(davlatlar):
#     print(davlat.upper())

# print('\nDavlatlarning poytaxtlari')
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())


""" 8 
Foydalanuvchidan istalgan davlatni kiritishni so'rang agar foydalanuvchi davlar kiritsa uning poytaxini, 
    poytaxt kiritsa uning davlatini konsulga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
    "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
"""
# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}

# savol = input("Davlat yoki shahar: ").lower()
# for k, v in davlatlar.items():
#     if savol == k:
#         print(f"{k.title()} ning poytaxti {v.title()} shaxri")
#     if savol == v:
#         print(f"{v.title()} shaxri {k.title()} ning poytaxti hisoblanadi")
# if savol not in davlatlar.keys() and savol not in davlatlar.values() :
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')


""" 9
Restoran menusi lug'atini tuzing(kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat
    buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda 
    bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
"""
# menu = {
#     "osh":15000,
#     "dimlama":12000,
#     "norin":20000,
#     "non":2000,
#     "choy":1000,
#     "salat":5000,
#     "shashlik":6000,
#     "musqaymoq":3000,
#     "pirojni":3000,
#     "somsa":5000
# }
# print("3 ta  taom nomini kiriting:")
# buyurtmalar = []
# for n in range(3) :
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar :
#     if buyurtma in menu :
#         print(f" {buyurtma.title()}  {menu[buyurtma]} so'm. ")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma.title()} yo'q.")



""" 8 
Foydalanuvchidan istalgan davlatni kiritishni so'rang agar foydalanuvchi davlar kiritsa uning poytaxini, 
    poytaxt kiritsa uning davlatini konsulga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
    "Bizda bunday dacvlat haqida ma'lumot yo'q" degan xabarni chiqaring.
"""
# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'
# }


# savol = input("Istalgan davlat yoki poytaxtni kiriting: ").lower()
# x = False
# for key, value in davlatlar.items():
#     if savol == value:
#         print(f"Siz yozgan {savol} shaxri {key.title()}da joylashgan")
#         x = True
#     elif savol == key:
#         print(f"Siz yozgan {savol} ning poytaxti {value.title()} ")
#         ex = True
# if x == False:
#     print("malumot yoq") 

menu = {
    "osh":15000,
    "dimlama":12000,
    "norin":20000,
    "non":2000,
    "choy":1000,
    "salat":5000,
    "shashlik":6000,
    "musqaymoq":3000,
    "pirojni":3000,
    "somsa":5000
}

narx = 0
zakaz = ""
yoq = []

for n in range(3):
    zakaz = input(f"{n+1}- taomni kiriting: ").lower()
    if zakaz in menu:
        narx += menu[zakaz]
        print(f"{zakaz} - {menu[zakaz]}")
    else:
        yoq.append(zakaz)

if narx != 0:
    print(f"Ummumiy narx {narx} so'm")

if yoq != []:
    print("Bizda quidagi taomlar yo'q")
    for i in yoq:
        print(i, end=" ")
        

