"""
Thame: Classlar bilan ishlash
"""

"""
Vazifa:

Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin
    va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga 
    tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. 
    Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.
Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, 
    Sotuvchi, Mijoz va hokazo)
Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan 
    Admin klassini yarating. 
Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga 
    "Foydalanuvchi bloklandi" degan matn chiqarsin.
"""

""" Javobi """

class Shahs:
    def __init__(self,ism,familya,passport,tyil):
        """Shahs haqida malumot"""
        self.ism =ism
        self.familya = familya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """Malumot beruvcgi funksia"""
        return f"{self.ism} {self.familya} , passport raqami>>> {self.passport}, {self.tyil}-yilda tug'ilgan "

class Talaba(Shahs):
    """Talaba klassi"""
    def __init__(self,ism,familya,passport,tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_fanlar(self):
        return self.fanlar
            
    def fanga_yozil(self,fan):
        self.fanlar.append(fan)
        return self.fanlar  
 
    def remove_fan(self,fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return f"Siz bu fanga yozilmagansiz"
    
class Fan:
    """Fan clasi"""
    def __init__(self,nom,tur):
        self.nom = nom
        self.tur = tur
    
    def get_name(self):
        return self.nom
    def get_info(self):
        return  f"{self.nom} fani {self.tur} fanlar qatoriga kiradi."
 
 

shahs1 = Shahs("Ulugbek","Xatamjonov","AB6414036",2001)
shahs2 = Shahs("Doniyor","Mamajonov","AB3457722",2005)
shahs3 = Shahs("Vali","Aliyev","AC5671988",1994)

talaba1 = Talaba("Mahmud","To'lanov","AB2908764",2000,1237783)
talaba2 = Talaba("Asadbek","Mirzaanvarov","AB4539855",1997,6458299)
talaba3 = Talaba("Aziz","Soliyev","AN5447123",1987,7864562)

fan1 = Fan("Algebra","aniq")
fan2 = Fan("Ona tili","ichtimoiy")
fan3 = Fan("Kimyo","tabiy")





