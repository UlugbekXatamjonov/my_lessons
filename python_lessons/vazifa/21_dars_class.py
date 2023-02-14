"""
Thame: Inkabsulyatsiya, klasslarning hususiyat va metodlari
"""

"""
Vazifa:
1) Texnika va Noutbook classlarini yarating. Noutbook texnika superclassi dan meros olgan.
    Shu class lar uchun ularning hususiyat  ko'ruvchi va o'zgartiruvchi metodlar yozing.
    Har ikkala classlar uchun yopiq xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi 
    va o'zgartiruvchi metodlar yozing.
"""

class Texnika:
    """ Texnikalar uchun class """
    def __init__(self, company, model, name, year):
        self.company = company
        self.model = model
        self.name = name
        self.__year = year
        
    def get_info(self):
        text = f"{self.company} kompaniyasining {self.model} modelidagi {self.name}i. "
        text += f"Ushbu mahsulot {self.__year}-yili ishlab chiqarilgan"
        return text
        
    def get_name(self):
        return self.name        

    def set_year(self, year):
        self.__year = year
        return self.__year
    

texnika1 = Texnika("LG", "RG200", "Televizor", 2019)

# print(texnika1.get_info())
# print(texnika1.get_name())

# print(texnika1.set_year(2024))
# print(texnika1.get_info())


class Noutbook(Texnika):
    """ Noutbook lar uchun maxsus class """
    def __init__(self, company, model, name, __year, protsessor, memory, g_card = False): # g_card -> Grafik karta
        Texnika.__init__(self, company, model, name, __year)
        
        self.protsessor = protsessor
        self.memory = memory
        self.__g_card = g_card
    
    def get_info(self):
        text = f"{self.company} kompaniyasining {self.model} modelidagi {self.name}i. "
        text += f"\nTexnik malumotlar: \nProtsessor: {self.protsessor} \nHotira: {self.memory}"
        if self.__g_card:
            text += f"\nGrafik karta: Bor"
        else: 
            text += f"\nGrafik karta: Yo'q"
        
        return text
    
    def set_g_card(self, card):
        self.__g_card = card
        return self.__g_card
        

noutbook1 = Noutbook("Asus", "TUF Gaming F506L", "Noutbook", 2021, "Core i7", "512 GB", True)
noutbook2 = Noutbook("HP", "Victus", "Noutbook", 2022, "Core i5", "1 TB")

# print(noutbook1.get_info())
# noutbook1.set_year(2019)
# print(noutbook1.get_info())

# print(noutbook1.get_info())
# print(noutbook2.get_info())

# noutbook2.set_g_card(True)
# print(noutbook2.get_info())









