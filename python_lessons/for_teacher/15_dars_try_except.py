"""
Thame: Try - except
"""

"""
<--- Dars tartibi ---> 
try-except
bir nechta except va xato turlari
else
finally


try - sizga xatolarni tekshirishga imkon beradi
except - sizga xatoni xal qilishga, va uning o'rniga boshqa ma'lumot chiqishiga imkon beradi
else - xato bo'lmaganda kodni bajarishga imkon beradi.

'try' bloki xatoga yo'l qo'yganligi sababli, 'except' bloki bajariladi.
'try' bloki bo'lmasa, dastur ishdan chiqadi va xatoga yo'l qo'yadi av dastur to'xtab qoladi:

https://www.tutorialsteacher.com/python/error-types-in-python

AssertionError -     Assert bayonoti bajarilmaganda ko'tariladi.
AttributeError -     Atribut tayinlashda ko'tarildi yoki mos yozuvlar bajarilmadi.
EOFError -   Input() funksiyasi faylning oxiri holatiga tushganda ko'tariladi.
FloatingPointError -     Suzuvchi nuqta operatsiyasi bajarilmaganda ko'tariladi.
GeneratorExit -  Jeneratorning close() usuli chaqirilganda ko'tariladi.
Import -     xatosi Import qilingan modul topilmaganda ko'tariladi.
IndexError -     Ketma-ketlik indeksi diapazondan tashqarida bo'lganda ko'tariladi.
KeyError -   Kalit lug'atda topilmasa ko'tariladi.
KeyboardInterrupt -  Foydalanuvchi uzilish tugmachasini bosganda ko'tariladi (Ctrl+c yoki o'chirish).
MemoryError -    Operatsiya xotirasi tugashi bilan ko'tariladi.
NameError -  O'zgaruvchi mahalliy yoki global miqyosda topilmasa ko'tariladi.
NotImplementedError -    Mavhum usullar bilan ko'tarilgan.
OSError -    Tizim ishi tizim bilan bog'liq xatolikka sabab bo'lganda ko'tariladi.
OverflowError -  Arifmetik amal natijasi koʻrsatish uchun juda katta boʻlganda koʻtariladi.
ReferenceError -     Axlat yig'ilgan referentga kirish uchun zaif havola proksi-serverdan foydalanilganda ko'tariladi.
RuntimeError -   Xato boshqa toifaga kirmasa ko'tariladi.
StopIteration -  iterator tomonidan qaytariladigan boshqa element yo'qligini bildirish uchun keyingi() funktsiyasi tomonidan ko'tariladi.
SyntaxError -    Sintaksis xatosiga duch kelganda tahlilchi tomonidan ko'tariladi.
IndentationError -   Noto'g'ri chiziq mavjud bo'lganda ko'tariladi.
TabError -   Qachonki chekinish mos kelmaydigan yorliqlar va bo'shliqlardan iborat bo'lsa ko'tariladi.
Tizim -  xatosi Tarjimon ichki xatoni aniqlaganida ko'tariladi.
SystemExit -     sys.exit() funksiyasi tomonidan ko'tarilgan.
TypeError -  Funktsiya yoki operatsiya noto'g'ri turdagi ob'ektga qo'llanilganda ko'tariladi.
UnboundLocalError -  Funksiya yoki usulda mahalliy o‘zgaruvchiga havola qilinganda ko‘tariladi, lekin bu o‘zgaruvchiga hech qanday qiymat bog‘lanmagan.
UnicodeError -   Unicode bilan bog'liq kodlash yoki dekodlash xatosi yuzaga kelganda ko'tariladi.
UnicodeEncodeError -     Kodlash paytida Unicode bilan bog'liq xatolik yuzaga kelganda ko'tariladi.
UnicodeDecodeError -     Unicode bilan bog'liq xato dekodlash vaqtida yuzaga kelganda ko'tariladi.
UnicodeTranslateError -  Unicode bilan bog'liq xato tarjima paytida yuzaga kelganda ko'tariladi.
ValueError -     Funktsiya to'g'ri turdagi, lekin noto'g'ri qiymatdagi argumentni olganida ko'tariladi.
ZeroDivisionError -  Bo'linish yoki modul operatsiyasining ikkinchi operandi nolga teng bo'lganda ko'tariladi.

else - xech qanday xatolik yuzaga kelmagan xollarda ishlatiladi

'try' - blokida xatolik bo'ladimi yoki yo'qmi, qat'iy 'finally' nazar bajariladi.

'raise' xato matnini dasturchiga o'zimiz hohlagan ko'rinishda ko'rsatishga imkon beradi

"""










