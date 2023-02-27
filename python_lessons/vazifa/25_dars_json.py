"""
Thame: Jsonlar bilan ishlash
"""

"""
Vazifa:
1)  Quidagi maqolalar ro'yhatini "maqolalar" nomli faylga json ko'rinishda saqlang va qaydadan chaqirib uni python kodi 
    ko'rinishida o'qing.

    maqolalar = [
        {
            "id": 1,
            "title": "Фикрлаш ва унинг бузилиши",
            "body": "Фикрлаш — индивиднинг билиш фаолиятидаги муҳим жа- раён бўлиб, атрофдаги борлиқнинг инсон онгида акс этишининг олий шакли ҳисобланади. Ҳис қилиш, тасаввур, идрок қилиш, билиш жараёнининг бошланғич босқичидир. Предметларнинг хоссалари ҳақидаги билимларни умумлаштириш тушунчаси фикрлашнинг асоси ҳисобланади.\r\n\r\nФикрлаш жараёни анализ (таҳлил) ва синтез, таққослаш, солиштириш, кўз ўнгига келтириш ва аниқлаштириш, умум- лаштириш, кейин эса тушунчанинг шаклланишига ўтиш босқичларидан ташкил топган. Фикрлашнинг моддий асоси — сўз ҳисобланади. Ҳар бир сўз маълум бир тушунчани бил- диради: масалан, аниқ (стол) ёки хаёлий (босқич). Фикрлаш субстратининг ёпиқ ёки хаёлий тушунчалар билан мос келиши қуйидагича фарқланади, яъни аниқ — тасвирий фикрлаш, хаё- лан — мантиқан фикрлаш. Охирги хусусият нутқи ривожлан- ган, мураккаб тушунчани умумлаштира оладиган катта ёшдаги одамларга хосдир.\r\n\r\nФикрлашнинг таркибий хусусиятларидан бири — бу ассо- циатив фаолиятдир.",
        },
        {
            "id": 2,
            "title": "Аутист – бахтсиз эмас",
            "body": "«Мен аутистман… Мен чарчадим… Мени тушунишмаганликларидан, ҳадеб тўғрилайверишларидан, жазолайверишларидан, танқид қилаверишларидан, ўзларига ўхшатиш учун дарс ўтаверишларидан… Ҳамма-ҳаммасидан чарчадим…\r\nҲа, мен аутистман! Ҳа, мен бошқачаман! Аммо тушунинглар, мен ёмон эмасман… мени тушунмасликларидан чарчадим… Мени боримча қабул қилмасликларидан чарчадим. Мендан «нормал» бўлишни кутишларидан чарчадим. Мен “нормал” эмасман! Тушунсанглар-чи! Мен аутистман. Мен бошқачаман. Ҳамманинг ўз тарозиси бор. Аммо аутистнинг дунёни қабул қилиш тарозиси бошқача. Ёмонмас! Яхшимас! Бошқача, тушуняпсизларми? Ҳамма нарсанинг ўлчов бирлиги бор: килограмм, метр, дақиқа. Аутистнинг ўлчов бирлиги ўзига хос, яна бир марта айтаман, ёмонмас, яхшимас, ўзига хос. Ўзингизга ўхшатишдан, аутистлар сизгни ўзига ўхшатишларини бас қилинг. Ёмон кўрманг, йиғламанг, бахтсиз деманг.\r\n\r\nАутист бахтсиз эмас!\r\nАутист болалар бирам ажойибки, олдингизда туриб сизни кўрмаслиги мумкин. ",
        },
        {
            "id": 6,
            "title": "Онг бузилиши синдромлари",
            "body": "Онгнинг бузилиши (хиралашуви) да беморда нафақат атроф реал дунё интиқосининг бузилиши, юз беради, балки ички боғлар (абстракт билиш) ҳамда ташқи (сезги ҳиссиёти) бевоси- та предмет ва ҳодисаларни акс эттириши ҳам бузилади. Онг- нинг бузилиш белгисига кўра беморнинг ўз шахсига нисбатан мўлжали ҳам бузилади, у ташқи дунёга аланглайди, вазиятни (вақт, жойини) баҳолай олмайди, борлиқ дунёдан юз ўгиради, атрофдагиларни қабул қила-олмайди, тафаккури ноаниқ ва тарқоқ онгнинг қисман ёки тўлиқсиз хиралашув даври ҳақида тўлиқ эслолмайди.\r\n\r\nОнг бузилишининг бошланишида қўйидаги синдромлар фарқланади. Онгнинг карахт бўлиш ҳолатининг уч даражаси фарқланади. Қисқа вақт давом этувчи онгнинг карахтлиги обнубуляция (юнонча пиЬ15 — булут) дейилади. Бунда ташқи таъсиротни қабул қилиш бир оз қийинлашади, онг худди булут ёки тутун билан ўралгандек бўлиб туради.\r\n\r\nКарахтлик — онгнинг сезиларли даражада бузилиши ташқи таъсиротларни қабул қилиш чегараси қисқаради. ",
        }
    ]

2)  Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring: 
    talaba_json = \"""{"ism":"Hasan","familiya":"Husanov","tyil":2000}\"""  # ❗❗❗  \ - belgisini o'chirib tashlang ❗❗❗

3) 2-mashqadagi o'zgaruvchini yangi sjon fayliga saqlang va qaytadan uni o'qib yana konsulga chiqaring.

"""


""" Javoblar """
import json
from pprint import pprint

""" 1 """
# maqolalar = [
#         {
#             "id": 1,
#             "title": "O‘zbekiston va Misr «yashil» energetika loyihalarini amalga oshirish bo‘yicha kelishib oldi",
#             "body": "O‘zbekiston rahbari ko‘hna va betakror Misr zaminida O‘zbekiston delegatsiyasiga ko‘rsatilgan samimiy qabul va mehmondo‘stlik uchun chuqur minnatdorlik bildirdi. Misr rahbariyati va xalqining ulkan yutuqlari O‘zbekistonni xursand qilayotganini aytdi. Bo‘lib o‘tgan muzokaralar chog‘ida yetakchilar ikki mamlakatda amalga oshirilayotgan keng ko‘lamli islohotlar - Yangi O‘zbekiston strategiyasi va Misrning «Yangi Respublika» dasturi bir-biriga hamohang ekani, yangi ish o‘rinlarini yaratish va kambag‘allikni qisqartirish, aholini ijtimoiy himoya qilish va shaharlar infratuzilmasini rivojlantirish borasidagi ishlar uyg‘unligi to‘g‘risida yakdil fikr bildirdi. «Biz prezident janoblari bilan ochiq, do‘stona va amaliy ruhda o‘tgan muloqotimiz davomida keng ko‘lamli hamkorligimizni rivojlantirishni muhokama qildik. Qarashlarimiz, yo‘nalishlarimiz birligini tasdiqladi.  Siyosiy, savdo-iqtisodiy, transport-logistika, madaniy-gumanitar, xavfsizlik va korrupsiyaga qarshi kurashish sohalarida ko‘p qirrali aloqalarimizni kengaytirish masalalari bo‘yicha ham kelishib oldik. ",
#         },
#         {
#             "id": 2,
#             "title": "Samsung yangi Galaxy S23 flagmanlarini taqdim etdi",
#             "body": "Samsung kompaniyasi yangi Galaxy S23 flagman smartfonlari seriyasini e’lon qildi. Kompaniya vakillari Galaxy Unpacked tadbiri chog‘ida smartfonlarni taqdim etdi. Marosim kompaniyaning YouTube kanalida namoyish etildi. Yangi smartfonlar qatoriga Galaxy S23, Galaxy S23+ va Galaxy S23 Ultra kiradi. Seriya qurilmalari Snapdragon 8 Gen 2 protsessori va 8 gigabayt operativ xotira bilan ta’minlangan.",
#         },
#         {
#             "id": 6,
#             "title": "Odamlar yana Oyga qaytmoqda. NASA so‘nggi 50 yildagi eng umidli loyihani ishga tushirdi",
#             "body": "Artemis dasturi nima va odamlar nega Oyga qaytmoqda? AQSh sobiq vitse-prezidenti Mayk Pens yaqin yillarda odamlar Artemis missiyasi doirasida Oyga qo‘nishini rasman va’da qilgandi. Bunday loyiha nega kerak bo‘lib qolganini NASA shunday tushuntirdi: «Biz Oyga ilmiy kashfiyotlar, iqtisodiy manfaatlar va tadqiqotchilarning yangi avlodini ilhomlantirish uchun qaytyapmiz. Artemis missiyasi kelajakdagi parvozlar uchun asosdir».",
#         }
# ]

# with open("D:/projects/my_lessons/python_lessons/vazifa/maqolalar.json", 'w') as f:
#     m_json = json.dump(maqolalar, f)

# with open("D:/projects/my_lessons/python_lessons/vazifa/maqolalar.json") as f:
#     m_python = json.load(f)

# for abs in m_python:
#     print(f"{abs['id']}-maqoola:")
#     print(f"{abs['title'].title()}")
#     print(f"\t{abs['body']}\n")
#     print("")


""" 2 """
# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 
# talaba  = json.loads(talaba_json)
# print(f"Talaba {talaba['ism']} {talaba['familiya']} {talaba['tyil']}- yili tug'ilgan.")


""" 3 """
# with open('D:/projects/my_lessons/python_lessons/vazifa/talaba.json', 'w') as f:
#     talaba_new_jsoon = json.dump(talaba_json, f)

# with open('D:/projects/my_lessons/python_lessons/vazifa/talaba.json')as f:
#     new_talaba = json.load(f)
# print(f"Talaba {talaba['ism']} {talaba['familiya']} {talaba['tyil']}- yili tug'ilgan.")





