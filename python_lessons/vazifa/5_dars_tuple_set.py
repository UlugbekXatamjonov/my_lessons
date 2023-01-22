"""
Thame: O'zgarmas ro'yhat(tuple), Set
""" 

"""
<--- Vazifa --->
1) oila deb nomlangan bo'sh o'zgarmas ro'yhatlarga o'z oila azolaringizni ismini qo'shing va konsulga chiqaring.com
	-so'ng oila azolarimizning 2 tasini ismini ro'yhatdan o'chirib tashalng va qolgan ismlarni konsulga chiqaring;
	-keyin esa qolgan ismlarni tahrirlab ulani familyasini ham qo'shing --> "Ali" > "Olimov Ali" . va konsulga chiqaring;
	-so'ngra avval o'chirib yuborgan ismlaringizni qaytadan ro'yhatgfa qo'shing va ularni ham konsulga chiqaring;

2) musbat_sonlar va manfiy_sonlar degan ikkita ro'yhat(list) yarating. so'ngra ularni birlashtirib yangi sonlar deb nomlangan
	ro'yhat yarating.
	-so'ngra ushbu ro'yhatni o'zgarmas ro'yhat shakliga keltiring va konsulga shu ro'yhatni va uning turini chiqaring;
	-keyin shu ro'yhatni o'chirib tashlang va uni qaytadan konsulga chiqarishga urinib ko'ring;

3) ismlar deb nomlangan ro'yhat(list) va sonlar deb nomlangan o'zgarmas ro'yhat yarating va ularni avval har birini keyin esa 
	birlashtirib ularning tuirni set ga almashtiring.

4) mevalar deb nomlangan ro'yhat(list ) yarating. Avval uni o'zgarmas ro'yhat turiga , keyin esa set turiga o'zgartiring va konsulga ularning 
turini chiqaring.
	-remove() yordamida 3 ta discard() yordamida 3 ta elementni o'chirib tashlang va ro'yhatni konsulga chiqaring.
	-va yangi 5 ta element qo'shing va ro'yhatni konsulga chiqaring;
	-so'ngra ro'yhatni tozalang va uni konsulga chiqaring;
	-keyin esa ro'yhatni o'chirib tashlang;

5) yuqorida yaratgan musbat_sonlar va manfiy_sonlar ro'yhatlarimizni set ko'rinishiga olib o'ting.
	-ularni sonlar degan yangi set ga birlashtiring va konsulga chiqaring;
	-har ikkolovida mavjud elementlarni avval musbat_sonlar setiga keyin esa manfiy_sonlar setiga birlashtirib, 
		har ikkolovini konsulga chiqaring;
"""

""" Javoblar """


""" 1 """
# oila = ('Ali', "Mahsuna", "Jasur", "Javohir", " Mohinur")
# print(oila)

# oila = list(oila)
# oila.remove('Ali')
# oila.remove('Jasur')
# print(oila)

# oila[0] = "Mahsuna Olimova"
# oila[1] = "Havohir Olimov"
# oila[2] = "Mohinur Olimova"
# print(oila)

# oila.append("Ali")
# oila.append("Jasur")
# oila = tuple(oila)
# print(oila)
# print(type(oila))


""" 2 """
# musbat_sonlar = [1,3,6,32,9,54,123,35]
# manfiy_sonlar = [-4,-6,-8,-21,-432,-1]
# sonlar = []
# sonlar.extend(musbat_sonlar)
# sonlar.extend(manfiy_sonlar)
# print(sonlar)

# sonlar = tuple(sonlar)
# print(sonlar)
# print(type(sonlar))

# del sonlar
# print(sonlar) # hatolik yuzaga keladi

""" 3 """
# ismlar = ['Olim', "Hasan", "Husan"]
# sonlar = (0,6.5,12,-9)

# ismlar = set(ismlar)
# sonlar = set(sonlar)
# print(type(ismlar), type(sonlar))

# sonlar.update(ismlar)
# print(sonlar)
# print(type(sonlar))

""" 4 """
# mevalar = ['olma', 'anor', 'bexi', 'olcha','limon','qovun','torvuz']
# mevalar = tuple(mevalar)
# print(type(mevalar))
# mevalar = set(mevalar)
# print(type(mevalar))

# mevalar.remove("olma")
# mevalar.remove("anor")
# mevalar.remove("bexi")
# mevalar.discard("olcha")
# mevalar.discard("limon")
# mevalar.discard("qovun")
# print(mevalar)

# mevalar.add("gilos")
# mevalar.add("o'rik")
# mevalar.add("kiwi")
# mevalar.add("apelsin")
# mevalar.add("xurmo")
# print(mevalar)

# mevalar.clear()
# print(mevalar)

# del mevalar
# print(mevalar)

""" 5 """
# musbat_sonlar = [1,3,6,32,9,54,123,35]
# manfiy_sonlar = [-4,-6,-8,-21,-432,-1]

# musbat_sonlar = set(musbat_sonlar)
# manfiy_sonlar = set(manfiy_sonlar)
# print(type(musbat_sonlar), type(manfiy_sonlar))

# sonlar = musbat_sonlar.union(manfiy_sonlar)
# print(sonlar)

# musbat_sonlar.update(manfiy_sonlar)
# print(musbat_sonlar, type(musbat_sonlar))

# manfiy_sonlar.update(musbat_sonlar)
# print(manfiy_sonlar, type(manfiy_sonlar))


