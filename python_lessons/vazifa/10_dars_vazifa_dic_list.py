"""
Thame: Dictionary-List(Lu'gatlar va Ro'yhatlar ustida ishlash)
"""

""" 
Vazifa 

1)  Ro'yhat ichida  ro'yhat
Telefonlar yoki koputerlar kompanialari va ularnig modellari ni ro'yhat ichida ro'yhat 
ko'rinishida jamlab ularni honsolga chiqaring

Misol:
lg = ['X5','Q7','X Power 1']
sumsung = ['S7',"A50"]
telefonlar = [lg, sumsung]
print(.....)

2)
<> lug'at ichida lug'at
Oilalar degan lu'gat yarating uning kalitlarilari o'rnida olila bo'sin, 
va o'sha oila kaliti o'rnida oilanging azosi bo'lsin va uning ichidagi lug'atda  
oila azosining malulotlari chiqib tursin

Misol:

oilalar = {
	'oila1':{
		'ota':{
			'ism':"Alijon",
            'familya':"Mamajonov",
            'yosh':'32',
            'kasb':"Duradgor",
		},
		'ona':{
			'ism':'Munisa',
            'familya':"Mamajonova",
            'yosh':'30',
            'kasb':"Tikuvchi",
		},
	'oila2':{
		...
	}
	}
}

print("For va if larni ishlatib barcha oila va uning zaolari haqida malumotlarni
chiroyli qilib chiqaring ")


3) Lug'at ichida ro'yhat
3 ta ko'chadagi do'stingizdan, 3 ta sinfdoshingizdan va 3 ta kursdagi o'rtog'ingiz 
haqidagi malumotlarni lugatga quyidagi kabi joylang va ichida ro'yhat ochib unga sevimli taomlarini kiritsin

Misol:
dostalar = {
	'sinfdoshlar':{
		'ali':['hotdog','osh','norin'],
        'anvar':['gamburger','lavash','chizburger'],
        'olim':['kabob','somsa','norin']
	},
	"dostlar":{
		'abbos':['qazi','somsa','norin']
	},
	...	
}
For va if larni ishlatib barcha dostlaringiz va ularning taomlari haqidagi malumotlarni
chiroyli qilib chiqaring


4) ro'yhat ichida lug'at

car_1 = {
 	'model':"S3",
 	'brend':"BMW",
 	'year':"2021",
 	'price':"23000",
}

car_2 = {
 	'model':"Nexia-3",
 	'brend':"Chevrolet",
 	'year':"2016",
 	'price':"16000",
}
cars = [car_1, car_2, ...]

"""

# ------------------------------
"""         Javoblar        """
# ------------------------------


""" 1 """
# lg = ['X5','Q7','X Power 1', 'Q52', 'Q62']
# sumsung = ['S7',"A50",'Zed 43','S9','A51','A52']
# redmi = ['A9','A8','A10','Note 10','Note 11','Note 12']
# telefonlar = [lg, sumsung, redmi]

# dell = ['Inspiron 3520','Inspiron 3030', 'Next 23']
# asus = ['TUF Gaming F15', 'TUF Pres A21', 'Vivo ZedBook']
# hp = ['Gaming Pavilion 2', 'VivoBook', 'VivoBook 3']
# noutbooklar = [dell, asus, hp]

# texnikalar = [telefonlar, noutbooklar]

# print(f" LG kompaniyasining telefon modellari:", end=' ')
# for  n in texnikalar[0][0]:
#     # print(n, end=', ')
#     if n == texnikalar[0][0][-1]:
#         print(f"{n}")
#     else:
#         print(f"{n}", end=', ')

# print(f" Sumsung kompaniyasining telefon modellari:", end=' ')
# for  n in texnikalar[0][1]:
#     if n == texnikalar[0][1][-1]:
#         print(f"{n}")
#     else:
#         print(f"{n}", end=', ')
        
# print(f" Redmi kompaniyasining telefon modellari:", end=' ')
# for  n in texnikalar[0][2]:
#     if n == texnikalar[0][2][-1]:
#         print(f"{n}")
#     else:
#         print(f"{n}", end=', ')


# print(f" Dell kompaniyasining komputer modellari:", end=' ')
# for  n in texnikalar[1][0]:
#     if n == texnikalar[1][0][-1]:
#         print(f"{n}")
#     else:
#         print(f"{n}", end=', ')
        
# print(f" Asus kompaniyasining komputer modellari:", end=' ')
# for  n in texnikalar[1][1]:
#     if n == texnikalar[1][1][-1]:
#         print(f"{n}")
#     else:
#         print(f"{n}", end=', ')
        
# print(f" HP kompaniyasining komputer modellari:", end=' ')
# for  n in texnikalar[1][2]:
#     if n == texnikalar[1][2][-1]:
#         print(f"{n}")
#     else:
#         print(f"{n}", end=', ')



""" 2 """

# oilalar = {
# 	'oila1':{
# 		'ota':{
# 			'ism':"Alijon",
#             'familya':"Mamajonov",
#             'yosh':'32',
#             'kasb':"Duradgor",
# 		},
# 		'ona':{
# 			'ism':'Munisa',
#             'familya':"Mamajonova",
#             'yosh':'30',
#             'kasb':"Tikuvchi",
# 		},
#         'aka':{
# 			'ism':'Nuraziz',
#             'familya':"Mamajonov",
#             'yosh':'18',
#             'kasb':"O'quvchi",
# 		},
#         'uka':{
# 			'ism':'Sardorbek',
#             'familya':"Mamajonov",
#             'yosh':'15',
#             'kasb':"O'quvchi",
# 		},
#     },
# 	'oila2':{
# 		'ota':{
# 			'ism':"Umarbek",
#             'familya':"Aliyev",
#             'yosh':'42',
#             'kasb':"Shifokor",
# 		},
# 		'ona':{
# 			'ism':'Nozima',
#             'familya':"Aliyeva",
#             'yosh':'39',
#             'kasb':"Hamshira",
# 		},
#         'aka':{
# 			'ism':'Jasur',
#             'familya':"Aliyev",
#             'yosh':'21',
#             'kasb':"Talaba",
# 		},
#         'uka':{
# 			'ism':'Abdulloh',
#             'familya':"Aliyev",
#             'yosh':'19',
#             'kasb':"O'quvchi",
# 		},
# 	}
# }


# for key, value in oilalar.items():
#     print(f"\n{key.upper()} haqida batafsil: ")
#     for k, v in value.items():
#         print(f" \n{k.title()} haqida maulot:")
#         for x, y in v.items():
#             print(f"  {x.title()}-{y.title()}")
            
               
""" 3 """
# dostalar = {
# 	'sinfdoshlar':{
# 		'ali':['hotdog','osh','norin'],
#         'anvar':['gamburger','lavash','chizburger'],
#         'olim':['kabob','somsa','norin'],
# 	},
# 	"dostlar":{
# 		'abbos':['osh','somsa','sho\'rva'],
#         'hasan':['lag\'mon','somsa','qazi'],
#         'husan':['lavash','osh','norin'],
# 	},
#     "kursdoshlar":{
# 		'umar':['lavash','gamburger','chizburger'],
#         'nodir':['osh','somsa','donar'],
#         'aziz':['kabob','somsa','qotirma'],
# 	},	
# }

# for key, value in dostalar.items():
#     print(f"\nMening {key.title()}imning yoqtirgan taomlari: ")
#     for k, v in value.items():
#         print(f"\n{k.title()}ning taomlari: ", end=' ')
#         for x in v:
#             if x == v[-1]:
# 				print(x)
# 			else:
# 				print(f"{x}", end=', ')
#     print('\n')

# for key, value in dostalar.items():
#     print(f"{key.title()}:")
#     for k, ismlar in value.items():
#         print(f"\n{k.title()} quidagi taomlarni yoqtirdi:", end=" ")
#         for taom in ismlar:
#             if taom == ismlar[-1]:
#                 print(f"{taom.title()}", end=".")
#             else:
#                 print(f"{taom.title()}", end=", ")
#     print('\n')


""" 4 """
# car_1 = {
#  	'model':"S3",
#  	'brend':"BMW",
#  	'year':"2021",
#  	'price':"23000",
# }
# car_2 = {
#  	'model':"Nexia-3",
#  	'brend':"Chevrolet",
#  	'year':"2016",
#  	'price':"16000",
# }
# car_3 = {
#  	'model':"Nexia-3",
#  	'brend':"Chevrolet",
#  	'year':"2016",
#  	'price':"16000",
# }
# car_4 = {
#  	'model':"Nexia-3",
#  	'brend':"Chevrolet",
#  	'year':"2016",
#  	'price':"16000",
# }

# cars = [car_1, car_2, car_3, car_4]

# for car in cars:
#     print("\n----- New car ------")
#     for key, value in car.items():
#         print(f"{key.title()} - {value.title()} ")

