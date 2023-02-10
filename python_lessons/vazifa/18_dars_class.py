"""
Thame: Classlar bilan ishlash
"""

""" 
Vazifa:

1) Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar
    (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart 
    qiymat bering (masalan, kilometer=0). Avto ga oid obyektning xususiyatlarini qaytaradigan 
    metodlar yozing. get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
    Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
    update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
"""


class Avto:
    def __init__(self,kom,model,rang,karobka,narh,yil):
        self.kom= kom
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.yil = yil
        self.km = 0

    def get_kom(self):
        return self.kom
    
    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.rang
    
    def get_karobka(self):
        return self.karobka

    def get_narh(self):
        return self.narh
    
    def get_yil(self):
        return self.yil
        
    def get_km(self):
        return self.km
        
    def get_info(self):
        return f"{self.kom} kompaniasining {self.model} modeldagi mashinasi. Rangi {self.rang}, boshqaruv {self.karobka}, {self.yil}-yili ishlab chiqarilgan,{self.km} km masofa yurgan, narxi {self.narh} $"

    def update_km(self):
        info = int(input("Yangi masofani kiriting:  "))
        self.km += info
        if self.km >= 100_000:
            self.narh -= 1_000
        elif self.km >= 500_000:
            self.narh += 2_000


car1 = Avto("Lexux","D4","qora","avtomat",23000,2019)
car2 = Avto("Kia","mako","oq","avtomat",18000,2020)
car3 = Avto("Porshe","G9 siler ","silver","avtomat",31000,2021)






