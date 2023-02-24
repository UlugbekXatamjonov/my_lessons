"""
Thame: Fayllar bilan ishlash
"""


"""
Birinchi qatorda open() funksiyasi yordamida faylni ochayapmiz. Bunda funksiyaga argument 
    sifatida fayl nomini berayapmiz. Bu yerda biz ochayotgan fayl va dasturimiz bir papkada bo'lishi muhim.
    open() funksiyasi faylni obyekt sifatida qaytaradi, as operatori yordamida esa biz obyektimizga 
    fayl deb nom berayapmiz.  Ikkinchi qatorda .read() metodi yordamida fayl obyektining tarkibidan 
    bizga kerakli matnni olib, yangi, PI o'zgaruvchisiga yuklayabmiz. with operatorining vazifasi biz fayl
    bilan ishlab bo'lganimizdan so'ng faylni yopish. Yuqoridagi misolda, 2-qatordan so'ng Python zudlik 
    bilan faylni yopadi.

Lekin, bu usul xavfli hisoblanadi va tavsiya qilinmaydi. Gap shundaki, open() funksiyasi yordamida 
    faylni ochganimizdan keyin, toki close() metodini chaqirgunga qadar faylimiz ochiq holatda turadi. 
    Agar, faylni vaqtida yopmasak, yoki fayl yopilmasidan avval dasturimiz to'xtab qolsa fayl 
    tarkibiga ziyon yetishi, ma'lumotlar yo'qotilishi mumkin.

    open() funksiyasiga with orqali murojat qilganimizda, faylimiz with blokining oxirigacha ochiq turadi, 
    va with tugashi bilan, fayl ham yopiladi.

    Matn faylda qanday saqlangan bo'lsa, huddi shu ko'rinishda konsolga chiqdi. 
    Saqlangan ma'lumot son bo'lsada, fayldan o'qiganimizda qaytgan qiymat matn ko'rinishida bo'ladi
    
Yuqorida biz faylni ochishda open() funksiyasidan foydalandik, va yagona argument sifatida fayl nomini berdik. 
    Bunda fayl faqatgina o'qish uchun ochiladi, unga yozib bo'lmaydi. Faylga ma'lumot yozish uchun open() 
    funksiyasiga murojat qilishda fayl nomidan tashqari yana bir argument beramiz. Ikkinchi argument faylni 
    aynan nima maqsadda ochishimizni bildiradi. 

-------------------------------------------------------------------------------------------------------------
w       open('file.txt','w')        Faylni yozish uchun ochish. Fayl mavjud bo'lmasa yangi fayl yaratiladi. 
                                    Fayl mavjud bo'lsa tarkibi o'chib ketadi

'r'     open('file.txt','r')        Faylni faqat o'qish uchun ochish (yozib bo'lmaydi)

'w+'    open('file.txt','w+')       Faylni o'qish va yozish uchun ochish. Fayl mavjud bo'lmasa yangi 
                                    fayl yaratiladi. Fayl mavjud bo'lsa tarkibi o'chib ketadi. 

'r+'    open('file.txt','r+')       Faylni o'qish va yozish uchun ochish.

'a'     open('file.txt','a')        Faylga ma'lumot qo'shish uchun ochish. 
                                    Fayl mavjud bo'lmasa yangi fayl yaratiladi.

'a+'    open('file.txt','a+')       Faylga ma'lumot qo'shish va o'qish uchun yozish. 
                                    Fayl mavjud bo'lmasa yangi fayl yaratiladi.

'x'     open('file.txt', 'x')       Fayl yaratadi, agar fayl mavjud bo'lsa, xatoni qaytaradi
-------------------------------------------------------------------------------------------------------------

❗❗❗ Diqqat!!! open() funksiyasini 'w' argumenti bilan chaqirganimizda ehtiyot bo'lishimiz kerak, 
    sababi agar bunday fayl mavjud bo'lsa, uning ichidagi barcha ma'lumotlar o'chib ketadi.

    Faylga yozayotgan ma'lumotlarimiz matn ko'rinishida bo'lishi kerak. Aks holda dasturimiz xato beradi.
❗❗❗ 


Agar dastur davomida turli o'zgaruvchilarni faylda saqlash talab qilinsa pickle modulidan foydalanamiz. 
    Pickle ma'lumotlarni biz qanday ko'rinishda bersak, shunday ko'rinishda faylga yozadi. 
    Yuqoridagi usuldan farqli ravishda, pickle yordamida yozilgan fayllarning tarkibini 
    Pythondan tashqarida ko'rib bo'lmaydi. 

Faylni ochishda esa, open() funksiyasiga ikkinchi argument sifatida 'wb' (write binary) beramiz, 
    ya'ni ikkilik sanoq tizimida yozishni ko'rsatamiz. Faylga yozish uchun esa pickle.dump() 
    metodidan foydalanamiz:


Pickle fayldan o'qish uchun open() funksiyasini 'rb' (read binary) argumenti bilan chaqiramiz. 
    O'zgaruvchilarni bitta faylga yozganimizda, har bir o'zgaruvchi alohida qatordan yoziladi. 
    Fayldan o'qishda ham har bir qatorni alohida o'qishimiz kerak bo'ladi.

    
Faylni o'chirish uchun siz OS modulini import qilishingiz va uning os.remove()funksiyasini 
    ishga tushirishingiz kerak:
Xatolik kelib chiqmasligi uchun faylni o'chirishdan oldin uning mavjudligini tekshirishingiz kerak.
Butun 'papka'ni o'chirish uchun  'os.rmdir()' usuldan foydalanamiz.

"""

