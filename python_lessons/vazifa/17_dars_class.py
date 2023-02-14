"""
Thame: Pythonda OOP va Class lar bilan tanishuv
"""
""""

Vazifa:

1) Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda 
    ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (username, foydalanuvchi ismi, email, va hokazo)
    Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan 
    ma'lumotlarni chiroyli qilib chiqarsin. 
    (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).
    Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
    
2) Oila classini yarating va 1-mashqdagi kabi shartlarni bajaring
"""
"""" Javoblar """

""" 1 """
# class User:
#     def __init__(self,name,username,gmail,number):
#         self.name = name
#         self.username = username 
#         self.gmail = gmail
#         self.number = number
        
#     def get_name(self):
#         """ Foydalanuvchi ismini qaytaruvchi metod """
#         return self.name
    
#     def get_uname(self):
#         """ Foydalanuvchi usernameni qaytaruvchi metod """
#         return self.username
    
#     def get_gmail(self):
#         """ Foydalanuvchi gmailini qaytaruvchi metod """
#         return self.gmail
    
#     def get_number(self):
#         """ Foydalanuvchi raqamini qaytaruvchi metod """
#         return self.number
    
#     def get_info(self):
#         """ Foydalanuvchi haqida ummumiy malumot qaytaruvchi metod """
#         return f"Foydalanuvchi: '{self.username}', ismi: '{self.name}', emaili: '{self.gmail}'', tel. raqami: '{self.number}'"


# user1 = User("Ulugbek","ulugbek17","xatamjonovulugbek17@gmail.com",993257417)
# user2 = User("Ali","olimovb","alimov@gmail.com",914567866)
# user3 = User("Usmon","usmonaziz","usmon1223@gmail.com",990997237)
# user4 = User("Bekzod","beki","turbekzod001@gmail.com",973498230)

# print(user1.get_name())
# print(user1.get_info())
# print(user1.get_number())
# print(user1.get_gmail())



""" 2 """

# class Oila:
#     """ Oila azolari haqida ma'lulot beruvchi class """
#     def __init__(self, ism, familya, tyil, kasb, telefon):
#         self.ism = ism
#         self.familya = familya
#         self.tyil = tyil
#         self.kasb = kasb
#         self.telefon = telefon
        
#     def full_name(self):
#         """ Insoning to'liq ismini qaytaruvchi metod """
#         return f"{self.ism} {self.familya}"
    
#     def full_info(self):
#         """ Inson haqida to'liq ma'lumot beruvchi metod  """
#         return f"{self.ism} {self.familya}. {self.tyil}-yilda tug'ilgan. Kasbi {self.kasb}, telefon raqami: {self.telefon}"

#     def get_number(self):
#         """ Insoning telefon raqamini qaytaruvchi metod """
#         return f"{self.ism}ning telefon raqami: {self.telefon}"
    
# inson1 = Oila("Olimjon", "Ayubov", 2001, "o'qtuvchi", "+998901234567")
# inson2 = Oila("hasanov", "Asadbek", 1998, "haydovchi", "+998772345566")

# print(inson1.full_name())
# print(inson1.full_info())
# print(inson1.get_number())












