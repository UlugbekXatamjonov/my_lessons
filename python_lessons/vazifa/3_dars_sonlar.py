"""
Thame:Sonlar bilan ishalsh, int()/str()/float() funksiyalari  
"""

"""
Vazifa:
1) Alanani uzunligini topuvchi dastur tuzing. Aylananing radiusini foydalanuvchidan so'rang.  
   Formulasi: S=2*pi*r  / pi=3.14 / r= radius
2) Doirani yuzini topuvchi dastur. Aylananing radiusini foydalanuvchidan so'rang.
   Formulasi: S=pi*r**2 / pi=3.14 / r = radius
3) Tog'ri burchakli uchburchakni katetlari ni foydalanuvchidan so'rab, shu uchburchakning gipotenuzasini hisoblaydigan dastur tuzing. 
   Formulasi: c**2 = a**2 + b**2   / a va b - katetlar, c - gipotenuza
4) Foydalanuvchidan ikkita son kiritishini so'rab shu kiritilgan sonlarning o'rta arifmetigini hisoblang.
   Formulasi: (a+b)/2
5) Foydalanuvchidan ikkita son kiritishini so'rab shu kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi
   bo'linmasi, o'rta arifmetigi va har ikkala sonning kvadrati va kubini aniqlang.
   Formulasi: a+b, a-b, a*b, a/b, (a+b)/2, a**2, a**3, b**2, b**3
6) Foydalanuvchidan ikkita A va B sonlarini kiritishini so'rang va sonlar qiymatini almashtirib konsulga chiqaring.
7) Foydalanuvchidan ikkita A, B va C sonlarini kiritishini so'rang va A ni qiymatini B ga , Bni qiymatinni C ga
   C ni qiymatini A ga almashtirib konsulga chiqaring
8) Foydalanuvchidan 'x' ni kiritishini so'rab quidagi 'y' ning qiymatini toping.
   y = 4*(x-3)**5-7*(x-3)**3+2
9) Quidagi ammalarning natijasini yaxlidlang:
   231/4.7    24/1.4   541/7.6
10) math va random modullaring har biridan 5 tadan funksiyani o'rganib, undan foydalanish(misol yozib kelish).
    Darsda ko'rganlarimizdan tashqari ! 
"""

"""  Javoblar """
import math
import random

""" 1  """
# r = int(input("Aylananing radiusini kiriting: "))
# pi = 3.14
# s = 2*pi*r
# print("Siz radiusini kiritga aylaning yuzi: ", s)

""" 2 """
# r = int(input("Doiraning radiusini kiriting: "))
# pi = 3.14
# s = pi*r**2
# print("Siz radiusini kiritga doiraning uzunligi: ", s)

""" 3 """
# a = int(input("Birinchi katetni kiriting: "))
# b = int(input("Ikkinchi katetni kiriting: "))
# c = round(math.sqrt(a**2+b**2),2)
# print("Katetlari", a, "va", b, "ga teng bo'lgan to'gri burchakli uchburchakning gipotenuzasi:", c)

""" 4 """
# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# arifmetik = (son1 + son2)/2
# print("Siz kiritgan", son1, "va", son2, "sonlaring o'rta arifmetigi: ", arifmetik)

""" 5 """
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# print("Yig'indi: ", a+b)
# print("Ayirma:", a-b)
# print("Bo'linma:", a/b)
# print("Ko'paytma:", a*b)
# print("O'rta arifmetik:", (a+b)/2)
# print("Kvadratlar a va b :", a**2, b**2)
# print("Kublar a va b :", a**3, b**3)

""" 6 """
# a = int(input("A sonni kiriting: "))
# b = int(input("B sonni kiriting: "))
# c = a
# a = b
# b = c
# print(a,b)

""" 7 """
# a = int(input("A sonni kiriting: "))
# b = int(input("B sonni kiriting: "))
# c = int(input("C sonni kiriting: "))
# d = c
# c = b
# b = a
# a = d
# print(a,b,c)

""" 8 """
# x = int(input("x ni kiriting: "))
# y = 4*(x-3)**5-7*(x-3)**3+2
# print("y =",y)

""" 9 """
# print(round(231/4.7,2))    
# print(round(24/1.4,2))  
# print(round(541/7.6,2))

""" 10 """
# print(random.uniform(1,10))
# print(random.triangular(2.1,12.3))
# print(random.betavariate(1, 2))
# print(random.gauss(9,7))
# print(random.normalvariate(1, 5))

# print(math.isinf(8))
# print(math.asinh(3))
# print(math.cos(16))
# print(math.exp(21))
# print(math.gcd(50,500))
