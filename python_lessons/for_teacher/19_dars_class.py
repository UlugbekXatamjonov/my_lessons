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
        persons.append(person)
        persons_count += 1     
        
    def update_persons_count(self, number):
        per