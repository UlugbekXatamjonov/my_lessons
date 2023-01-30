
def password_func():
    """ Parol tizimi """
    ha = 0
    print("Assalomu aleykum")
    parol1 = input("Iltimos o'zingiz uchun parol kiriting(parol eng kamida 8 ta belgidan iborat bo'lsin): ")
    parol2 = input("Parolni yana bir bor takrorlang: ")
    if parol1 == parol2 and len(parol1) >= 8:
        print("Parol muvafaqqiyatli o'rnatildi")
        ha = 1
    else:
        if len(parol1) < 8:
            print("Xatolik ! Eng kamida 8 ta belgi bo'lishi kerak")
        else:
            print("Xatolik ! Iltimos parolni boshqatdan kiriting")
    if ha == 1:
        parol3 = input("Tizim`ga kir`ish uchun parolingizni kiriting: ")
        if parol1 == parol3:
            print("Hush kelibsiz Admin")
        else:
            print("Parol xato !!!!")
            
            
            
            