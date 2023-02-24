"""
Thame: Jsonlar bilan ishlash
"""



"""
JSON - JavaScript Object Notation
Dastur va server orasidagi ma'lumotlar aynan JSON ko'rinishida uzatiladi.

Dasturlarimiz davomida ma'lumotlarni JSON ko'rinishida saqlashimiz, 
    internet orqali boshqa foydalanuvchilarga, dasturlarga yoki serverga yuborishimiz, 
    JSON fayllarni Pythonda ochib, unga ishlov berishimiz va turli amallar bajarishimiz mumkin.

JSON o'zgaruvchilar, tarkibidan qat'iy nazar matn ko'rinishida saqlanadi.

JSON ma'lumotlar va fayllar bilan ishlash uchun Pythonda maxsus json moduli bor. >>> import json
Ma'lumotlarni JSON matniga o'tkazish uchun ikki funksiyadan foydalanamiz: 
    json.dumps(x) — berilgan x o'zgaruvchini JSON matniga o'zgartiradi
    json.dump(x,fayl) — berilgan x o'zgaruvchini JSON ga o'zgartirib, ko'rsatilgan faylga saqlaydi.

    
Python-dan JSON-ga aylantirilganda, Python ob'ektlari JSON (JavaScript) ekvivalentiga aylantiriladi:

Python	JSON

dict	Object
list	Array
tuple	Array
str	    String
int	    Number
float	Number
True	true
False	false
None	null


JSON formatidagi ma'lumotlarni Pythondagi ma'lumot turiga keltirish uchun json.loads() yoki 
    json.load() funksiyalaridan foydalanamiz. Yuqoridagi ka'bi, json.loads() funksiyasi 
    to'g'ridan-to'g'ri JSON matn bilan ishlasa, json.load() funksiyasi JSON fayllarni o'qish uchun ishlatiladi.

json.loads() - Bu funksiya parametr sifatida JSON matn qabul qiladi va Python o'zgaruvchiga o'tkazadi.
json.load() - Bu funksiya JSON fayllarning tarkibini Pythonga yuklab olish uchun ishlatiladi. 

"""

