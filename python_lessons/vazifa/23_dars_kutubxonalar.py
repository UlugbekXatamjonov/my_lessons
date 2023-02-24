"""
Thame: Pythonda Kutubxonalar, dates, math, RegEx...
"""

""" 
Vazifa 

1) Foydalanuvchidan tug'ilgan kuni, sanasini so'rab, unga tug'ilgan vaqtidan ayni 
    vaqtgacha o'tgan, vaqtni soat va minutigacha aniqlikda hisob qaytaring.
2) Insonlarning yoshi uchun regex yarating.
3) Aynan O'zbekiston aloqa operatorlari raqamlariga mos regex yarating.
"""

import re 
import datetime

""" 1 """
# def bithday():  # sourcery skip: do-not-use-bare-except
#     """ Insonning tug'ilgan kuni haqidagi malumotlarni qaytaradigan funksiya """
  
#     ism  = input("Assalomu aleykum Mr! \nIltimos ismingizni kiriting: ")

#     while True:
#         try:
#             t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#             if t_yil > 1890 and t_yil <= 2023:
#                 break
#             else:
#                 print("Siz mantiqqa to'g'ri kelmaydigan yil kiritdingiz")
#         except ValueError:
#             print("Xatolik !!! Iltimos butun va manfiy son kiriting !")
#         except:
#             print("Xatolik !!! Iltimos qaytadan harakat qiling !")
        
#     while True:
#         try:
#             t_oy = int(input("tug'ilgan oyingizni kiriting: "))
#             if t_oy <= 12 and t_oy >=1:
#                 break
#             else:
#                 print("Ma'lumot kiritishda xatolik bo'ldi !!!")
#         except ValueError:
#             print("Xatolik !!! Iltimos butun va manfiy son kiriting !")
#         except:
#             print("Xatolik !!! Iltimos qaytadan harakat qiling !")
        
#     while True:
#         try:
#             t_kun = int(input("tug'ilgan kuningizni kiriting: "))
#             if t_kun <= 31 and t_kun >=1:
#                 break
#             else:
#                 print("Ma'lumot kiritishda xatolik bo'ldi !!!")
#         except ValueError:
#             print("Xatolik !!! Iltimos butun va manfiy son kiriting !")
#         except:
#             print("Xatolik !!! Iltimos qaytadan harakat qiling !")
    
#     while True:
#         try:
#             t_soat = int(input("tug'ilgan soatingizni kiriting: "))
#             if t_soat <= 23 and t_soat >=1:
#                 break
#             else:
#                 print("Ma'lumot kiritishda xatolik bo'ldi !!!")
#         except ValueError:
#             print("Xatolik !!! Iltimos butun va manfiy son kiriting !")
#         except:
#             print("Xatolik !!! Iltimos qaytadan harakat qiling !")
        
    
#     t_sana = datetime.datetime(t_yil, t_oy, t_kun, t_soat, 00, 00)
#     # print(t_sana)

#     bugun =  datetime.datetime.now()
#     # print(bugun)

#     yosh = bugun - t_sana # o'rtadagi faqrni kunlar hisobida topib olamiz
#     # print(yosh)

#     yil = round(yosh.days/365)
#     oy = round(yosh.days/365*12)
#     kun = yosh.days
#     soat = round(yosh.total_seconds()*60*24)
#     minut = round(yosh.total_seconds()*60)
#     sekund = round(yosh.total_seconds())
    
#     text = f"Hurmatli {ism.title()} siz tu'gilgan vaqtdan so'ng: \n{yil} yil, \n{oy} oy, \n{kun} kun, \n{soat} soat, \n{minut} minut, \n{sekund} sekund o'tdi."
#     print(text)
#     # return text

# bithday()


""" 2 """
# yaer_regex = '^[1-9]?[0-9]?[0-9]$'


""" 3 """
# tel_regex = '^[\+]?[9]{2}[8]?[(]?[0-9]{2}?[)]?[-][0-9]{3}?[-][0-9]{2}?[-][0-9]{2}$'
""" Quidagi formatdagi raqamlar uchun:
    +998(33)-345-45-45
    +99833-345-45-45

    ❗❗❗ Aynan uzb kodlari uchun emas !
"""

# print(re.match(tel_regex, '+998(33)-345-45-45'))
# print(re.match(tel_regex, '+99833-345-45-45'))
# print(re.match(tel_regex, '+998333454545'))
# print(re.match(tel_regex, '333454545'))








