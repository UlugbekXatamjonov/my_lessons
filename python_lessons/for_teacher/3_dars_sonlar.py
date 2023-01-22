"""
Thame:Sonlar bilan ishalsh, int()/str()/float() funksiyalari  
"""


"""  
Dars tartibi:

sonlar turlari > int float complex
o'nlik va butun son turlari
arifmetik amallar
sonni kvadratga ko'tarish
sonni ildizdan chiqarish 
sonni yaxlidlash
random moduli
f"" bilan ishlash
int()/ str()/ float() funksiyalari
bir nechta o'zgaruvchi yaratish
ko'p honali sonlar
darsda masalar yechish
"""


"""
✔ random
👇👇👇 random modulining ayrim funksiyalari 👇👇👇
link -->  https://www.w3schools.com/python/module_random.asp

seed() Tasodifiy sonlar generatorini ishga tushirish 
getstate() Tasodifiy sonlar generatorining joriy ichki holatini qaytaradi 
setstate() Tasodifiy sonlar generatorining ichki holatini tiklaydi 
getrandbits() Tasodifiy bitlarni ifodalovchi raqamni qaytaradi 
randrange() Tasodifiy sonni qaytaradi berilgan diapazon o'rtasida 
randint() Berilgan diapazon orasidagi tasodifiy sonni qaytaradi 
Choice() Berilgan ketma-ketlikdan tasodifiy elementni qaytaradi 
options() Berilgan ketma-ketlikdan tasodifiy tanlangan ro'yxatni qaytaradi 
shuffle() Ketmani oladi va ketma-ketlikni qaytaradi tasodifiy tartibda 
sample() Ketma-ketlikning berilgan namunasini qaytaradi 
random() 0 va 1 orasidagi tasodifiy float sonini qaytaradi 
uniform() Ikki berilgan parametr orasidagi tasodifiy float sonini qaytaradi 
triangular() Ikki berilgan parametr orasidagi tasodifiy float sonini qaytaradi , 
    siz boshqa ikkita parametr orasidagi oʻrta nuqtani belgilash uchun rejim parametrini ham oʻrnatishingiz mumkin 
betavariate() Beta taqsimotiga asoslangan 0 va 1 oʻrtasidagi tasodifiy float sonini qaytaradi (biz ed in statistics) 
expovariate() Eksponensial taqsimotga asoslangan tasodifiy float sonini qaytaradi (statistikada ishlatiladi) 
gammavariate() Gamma taqsimotiga asoslangan tasodifiy float sonini qaytaradi (statistikada ishlatiladi) 
gauss() Gauss taqsimoti (ehtimollar nazariyalarida qo'llaniladi) 
lognormvariate() Log-normal taqsimotga asoslangan tasodifiy float sonini qaytaradi (ehtimollar nazariyalarida qo'llaniladi) 
normalvariate() Oddiy taqsimotga asoslangan tasodifiy float sonini qaytaradi (ehtimol nazariyalarida qo'llaniladi) 
vonmisesvariate() Von Mises taqsimotiga asoslangan tasodifiy float sonini qaytaradi (yo‘nalish bo‘yicha statistikada qo‘llaniladi) 
paretovariate() Pareto taqsimotiga asoslangan tasodifiy float sonini qaytaradi (ehtimollar nazariyalarida qo‘llaniladi) 
weibullvariate() Weibull asosida tasodifiy float sonini qaytaradi tarqatish (statistikada ishlatiladi)


✔ math
👇👇👇 math modulining ayrim funksiyalari 👇👇👇
link --> https://www.w3schools.com/python/module_math.asp

math.acos() Raqamning yoy kosinusini qaytaradi
math.acosh() Sonning teskari giperbolik kosinusini qaytaradi
math.asin() Sonning yoy sinusini qaytaradi
math.asinh() Sonning teskari giperbolik sinusini qaytaradi
math.atan() Radyandagi sonning yoy tangensini qaytaradi
math.atan2() y/x ning yoy tangensini radianlarda qaytaradi
math.atanh() Sonning teskari giperbolik tangensini qaytaradi
math.ceil() Raqamni eng yaqin butun songacha yaxlitlaydi
math.comb() n ta elementdan takror va tartibsiz tanlash usullari sonini qaytaradi
math.copysign() Birinchi parametrning qiymati va ikkinchi parametrning belgisidan iborat floatni qaytaradi
math.cos() Raqamning kosinusini qaytaradi
math.cosh() Sonning giperbolik kosinusini qaytaradi
math.degrees() Burchakni radiandan gradusga aylantiradi
math.dist() Ikki nuqta (p va q) orasidagi Evklid masofasini qaytaradi, bu erda p va q bu nuqtaning koordinatalaridir.
math.erf() Raqamning xato funksiyasini qaytaradi
math.erfc() Raqamning to'ldiruvchi xato funksiyasini qaytaradi
math.exp() X darajasiga ko'tarilgan E ni qaytaradi
math.expm1() Ex - 1ni qaytaradi
math.fabs() Raqamning mutlaq qiymatini qaytaradi
math.factorial() Raqamning faktorialini qaytaradi
math.floor() Raqamni eng yaqin butun songacha yaxlitlaydi
math.fmod() x/y ning qolgan qismini qaytaradi
math.frexp() Belgilangan sonning mantis va ko'rsatkichini qaytaradi
math.fsum() Har qanday takrorlanadigan barcha elementlarning yig'indisini qaytaradi (kordellar, massivlar, ro'yxatlar va boshqalar).
math.gamma() X da gamma funksiyasini qaytaradi
math.gcd() Ikki butun sonning eng katta umumiy boʻluvchisini qaytaradi
math.hypot() Evklid normasini qaytaradi
math.isclose() Ikki qiymat bir-biriga yaqin yoki yo'qligini tekshiradi
math.isfinite() Raqamning chekli yoki chekli emasligini tekshiradi
math.isinf() Raqam cheksiz yoki cheksiz ekanligini tekshiradi
math.isnan() Qiymat NaN (raqam emas) yoki yo'qligini tekshiradi
math.isqrt() Kvadrat ildiz sonini pastga qarab eng yaqin butun songa yaxlitlaydi
math.ldexp() math.frexp() ning teskarisini qaytaradi, bu berilgan x va i raqamlarining x * (2**i) ga teng
math.lgamma() X ning log gamma qiymatini qaytaradi
math.log() Sonning natural logarifmini yoki sonning logarifmini asosga qaytaradi
math.log10() x ning 10 ta asosiy logarifmini qaytaradi
math.log1p() 1+x ning natural logarifmini qaytaradi
math.log2() x ning 2 ta asosiy logarifmini qaytaradi
math.perm() n ta elementdan tartibli va takrorlanmasdan k ta elementni tanlash usullari sonini qaytaradi
math.pow() x qiymatini y darajasiga qaytaradi
math.prod() Takrorlanadigan barcha elementlarning mahsulotini qaytaradi
math.radians() Daraja qiymatini radianga aylantiradi
math.remainder() Numeratorni maxrajga toʻliq boʻlinishi mumkin boʻlgan eng yaqin qiymatni qaytaradi
math.sin() Sonning sinusini qaytaradi
math.sinh() Sonning giperbolik sinusini qaytaradi
math.sqrt() Raqamning kvadrat ildizini qaytaradi
math.tan() Raqamning tangensini qaytaradi
math.tanh() Sonning giperbolik tangensini qaytaradi
math.trunc() Raqamning kesilgan butun son qismlarini qaytaradi

"""

