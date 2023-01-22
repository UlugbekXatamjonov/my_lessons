"""
Thame: Matnlar(String) bilan ishlash
"""

"""
<--- Dars tartibi --->

matnlar haqida
type()
str() haqida
'' va ""
Atributlar / metodlar
strip()
f"" bn ishlash
input() funksiyasi
len() funksiyasi
matnni tekshirish
matnni kesib chiqarish
replace() metodi
split()
matnlarni qo'shish
maxsus belgilar
unicode --> https://unicode-table.com/en/
emojilardan foydalanish

👇👇👇 string method / matn metodlari 👇👇👇
link --> https://www.w3schools.com/python/python_ref_string.asp

kapitalize() Birinchi belgini katta harfga aylantiradi
casefold() satrni kichik harfga aylantiradi
center() Markazlangan satrni qaytaradi
count() Belgilangan qiymat satrda necha marta sodir bo'lishini qaytaradi
encode() satrning kodlangan versiyasini qaytaradi
endswith() Agar satr belgilangan qiymat bilan tugasa, true qiymatini qaytaradi
expandtabs() Satrning yorliq hajmini o'rnatadi
find() Belgilangan qiymat uchun satrni qidiradi va u topilgan joyni qaytaradi
format() Satrdagi belgilangan qiymatlarni formatlaydi
format_map() Satrdagi belgilangan qiymatlarni formatlaydi
index() Belgilangan qiymat uchun satrni qidiradi va u topilgan joyni qaytaradi
isalnum() Agar satrdagi barcha belgilar alfanumerik bo'lsa, True qiymatini qaytaradi
isalpha() Agar satrdagi barcha belgilar alifboda bo'lsa, True qiymatini qaytaradi
isascii() Agar satrdagi barcha belgilar ascii belgilar bo'lsa, True qiymatini qaytaradi
isdecimal() Agar satrdagi barcha belgilar oʻnli kasr boʻlsa, True qiymatini qaytaradi
isdigit() Agar satrdagi barcha belgilar raqam bo'lsa, True qiymatini qaytaradi
isidentifier() agar satr identifikator bo'lsa, True qiymatini qaytaradi
islower() Agar satrdagi barcha belgilar kichik bo'lsa, True qiymatini qaytaradi
isnumeric() Agar satrdagi barcha belgilar raqamli bo'lsa, True qiymatini qaytaradi
isprintable() Agar satrdagi barcha belgilar chop etilishi mumkin bo'lsa, True qiymatini qaytaradi
isspace() Agar satrdagi barcha belgilar boʻsh joy boʻlsa, True qiymatini qaytaradi
istitle() Agar satr sarlavha qoidalariga rioya qilsa, True qiymatini qaytaradi
isupper() Agar satrdagi barcha belgilar katta bo'lsa, True qaytaradi
join() takrorlanadigan elementlarni satrga aylantiradi
ljust() Satrning chapga asoslangan versiyasini qaytaradi
low() satrni kichik harfga o'zgartiradi
lstrip() Satrning chap trim versiyasini qaytaradi
maketrans() Tarjimalarda foydalanish uchun tarjima jadvalini qaytaradi
partition() satr uch qismga ajratilgan kortejni qaytaradi
replace() Belgilangan qiymat belgilangan qiymat bilan almashtirilgan satrni qaytaradi
rfind() Belgilangan qiymat uchun satrni qidiradi va u topilgan joyning oxirgi holatini qaytaradi
rindex() Belgilangan qiymat uchun satrni qidiradi va u topilgan joyning oxirgi holatini qaytaradi
rjust() satrning o'ngga asoslangan versiyasini qaytaradi
rpartition() satr uch qismga bo'lingan kortejni qaytaradi
rsplit() Belgilangan ajratuvchida satrni ajratadi va ro'yxatni qaytaradi
rstrip() Satrning o'ng trim versiyasini qaytaradi
split() Belgilangan ajratuvchida satrni ajratadi va ro'yxatni qaytaradi
splitlines() Satrni qatorlar oralig'ida ajratadi va ro'yxatni qaytaradi
startswith() Agar satr belgilangan qiymatdan boshlansa, true qiymatini qaytaradi
strip() Stringning kesilgan versiyasini qaytaradi
swapcase() Harflarni almashtiradi, kichik harflar katta va aksincha
title() Har bir so'zning birinchi belgisini katta harfga o'zgartiradi
translate() Tarjima qilingan qatorni qaytaradi
upper() satrni katta harfga aylantiradi
zfill() satrni boshida belgilangan 0 qiymatlar soni bilan to'ldiradi

"""

""" Maxsus belgilar """
# \'    ' belgisi uchun
# \"    " belgisi uchun
# \n    Yangi qator
# \r    Yangi qator
# \t    Tab tashlab beradi
# \b    bo'shqilni yo'qotib beradi


