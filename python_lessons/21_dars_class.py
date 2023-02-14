"""
Thame: Inkabsulyatsiya, klasslarning hususiyat va metodlari
"""

"""
Obyektga Yo'naltirilgan Dasturlashning tamoyillaridan biri bu inkapsulyatsiya, 
    ya'ni obyektning xususiyatlarga to'g'ridan-to'g'ri (nuqta orqali) murojat qilishni 
    va ularning qiymatini o'zgartirishni taqiqlab qo'yish. Pythonda bunday yopiq 
    xususiyatlarning nomi ikki pastki chiziq bilan boshlanadi:
"""

# from uuid import uuid4

# class Avto:
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
            
# avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)

# print(avto1.model)

"""
def get_km(self):
        return self.__km
    
def get_id(self):
    return self.__id
"""
# print(avto1.__km)
# print(avto1.get_km())


"""
    # def add_km(self,km):
    #     if km>=0:
    #         self.__km += km
    #     else:
    #         print("Mashina km kamaytirib bo'lmaydi")
"""
# avto1.add_km(1500)
# print(avto1.get_km())


"""
Avvalgi darslarimizda biror klassdan yaratilgan har bir obyektning xususiyatlarini klass 
    ichidagidef __init__() medoti yordamida berayotgan edik. Bu metod qanday ishlaydi? 
    Biz har gal klassga murojat qilganimizda klass aynan shu __init__metodini ishga tushiradi va 
    biz bergan xususiyatlar bilan yangi obyekt yaratadi.
    Pythonda xususiyatlarni nafaqat obyektga balki to'g'ridan-to'g'ri klassga ham yuklash 
    imkoniyati mavjud. Bunda klassning xususiyatiga berilgan qiymat barcha obyektlar uchun umumiy bo'ladi. 
    Bu xususiyatni bir obyekt orqali o'zgartirilganda shu klassga oid barcha obyektlarda ham uning qiymati 
    o'zgaradi. Klassga oid xususiyatlar def __init__() metodidan avval e'lon qilinadi.
"""

"""
num_avto = 0
    Avto.num_avto += 1
"""
# print(avto1.num_avto)


""" Klassga oid xususiyatlar ham huddi yuoqridagi kabi nomidan avval 
    ikki pastki chiziq qo'shish bilan inkapsulyatsiya qilinadi
    
    Klasslarning o'ziga xos metodlari ham bo'lishi mumkin. Misol uchun yuqoridagi 
    num_avto xususiyatini ko'rish uchun alohida metod yozishimiz mumkin. 
    Klassga oid metodlar @classmethod dekoratori bilan boshlanadi va obyektga oid 
    metodlardan farqli ravishda self emas cls (class) argumentini qabul qiladi.
"""

"""
@classmethod
    def get_num_avto(cls):
        return cls.__num_avto
"""
# print(Avto.get_num_avto())


"""
Vazifa:
1) Texnika va Noutbook classlarini yarating. Noutbook texnika superclassi dan meros olgan.
    Shu class lar uchun ularning hususiyat  ko'ruvchi va o'zgartiruvchi metodlar yozing.
    Har ikkala classlar uchun yopiq xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi 
    va o'zgartiruvchi metodlar yozing.
    
"""




