"""
Thame: Classlar bilan ishlash
"""

""" Vazifa 

Oila va Inson klasini yarating va dars davomida classlar ustida ishlaganimiz dek shu klaslar bilan ishlang.
"""

class Oila():
    """ Oila classi """
    def __init__(self, name):
        self.name = name
        self.persons = []
        self.persons_count = 0  

    def get_info(self):
        return f"{self.name} oilasida {self.persons_count} kishi yashaydi"
    
    def add_person(self, person):
        self.persons.append(person)
        self.persons_count += 1     
        
    def update_persons_count(self, number):
        self.persons_count = number # keyin yangi sonni qo'shamiz
        
    def about_persons(self):
        return [person.get_info_person() for person in self.persons]
        
oila1  = Oila("Abdullayevlar")   
        
class Person():
    """ Inson haqidagi classi """
    def __init__(self, full_name, age, job, country):
        self.full_name = full_name
        self.age = age
        self.job = job
        self.country = country
            
    def get_info_person(self):
        return f"{self.full_name} {self.country}da yashaydi. Hozirda {self.age} da, kasbi {self.job}."
        
person1 = Person("Abdullayev Aboos", 34, "Mehanik", "O'zbekiston")
person2 = Person("Abdullayeva Nargiza", 30, "Hamshira", "O'zbekiston")    
        
        
oila1.add_person(person1)
oila1.add_person(person2)
# print(oila1.get_info())

oila1.update_persons_count(5) # oiladagi azolar sonini o'zgartiramiz
print(oila1.get_info())
      
print(oila1.about_persons())  
        
        
        