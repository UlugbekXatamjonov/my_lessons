"""
Thame: Inkabsulyatsiya, klasslarning hususiyat va metodlari
"""


"""
Obyektga Yo'naltirilgan Dasturlashning tamoyillaridan biri bu inkapsulyatsiya, 
    ya'ni obyektning xususiyatlarga to'g'ridan-to'g'ri (nuqta orqali) murojat qilishni 
    va ularning qiymatini o'zgartirishni taqiqlab qo'yish. Pythonda bunday yopiq 
    xususiyatlarning nomi ikki pastki chiziq bilan boshlanadi:

Avvalgi darslarimizda biror klassdan yaratilgan har bir obyektning xususiyatlarini klass 
    ichidagidef __init__() medoti yordamida berayotgan edik. Bu metod qanday ishlaydi? 
    Biz har gal klassga murojat qilganimizda klass aynan shu __init__metodini ishga tushiradi va 
    biz bergan xususiyatlar bilan yangi obyekt yaratadi.
    Pythonda xususiyatlarni nafaqat obyektga balki to'g'ridan-to'g'ri klassga ham yuklash 
    imkoniyati mavjud. Bunda klassning xususiyatiga berilgan qiymat barcha obyektlar uchun umumiy bo'ladi. 
    Bu xususiyatni bir obyekt orqali o'zgartirilganda shu klassga oid barcha obyektlarda ham uning qiymati 
    o'zgaradi. Klassga oid xususiyatlar def __init__() metodidan avval e'lon qilinadi.

Klassga oid xususiyatlar ham huddi yuoqridagi kabi nomidan avval 
    ikki pastki chiziq qo'shish bilan inkapsulyatsiya qilinadi
    
    Klasslarning o'ziga xos metodlari ham bo'lishi mumkin. Misol uchun yuqoridagi 
    num_avto xususiyatini ko'rish uchun alohida metod yozishimiz mumkin. 
    Klassga oid metodlar @classmethod dekoratori bilan boshlanadi va obyektga oid 
    metodlardan farqli ravishda self emas cls (class) argumentini qabul qiladi.
"""

