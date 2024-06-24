"""
23//06//2023
Dars: 10
Mavzu: IF-ELSE
Author: Mujibali Temiraliyev
"""


"""TARMOQLANISH"""
# =============================================================================
# # Shu vaqtgacha yozgan dasturlarimizga e'tibor bersangiz, dasturimiz 
# # yuqoridan pastga qarab qatorma-qator bajarilib keldi. Bu chiziqli
# # dastur deyiladi. Voqelikda esa aksar dasturlar ma'lum bir shart bajarilishi 
# # (yoki bajarilmaganiga) ko'ra kodning bir qismidan boshqa qismiga "sakrab" 
# # o'tishi tabiiy hol. Dasturlashda bu tarmoqlanish deb ataladi.
# =============================================================================


"""if OPERATORI"""
# =============================================================================
# # if so'zi ingliz tilidan "agar" deb tarjima qilinadi va deyarli barcha 
# # dasturlash tillarida shartlarni yozish uchun foydalaniladi. 
# # Keling quyidagi misolni ko'ramiz. Bizda avtolar ro'yxati bo
# 
# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar: # avtolar ichidagi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ... 
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.
# =============================================================================

"""TRUE/FALSE"""
# =============================================================================
# # Yuqorida shartni tekshirish uchun == operatoridan foydalandik. Bu 
# # operatorni oddiy tilga tarjima qilsak "tengmi?" degan ma'noni beradi. 
# # Agar shartning ikki tarafidagi qiymatlar teng bo'lsa ifoda TRUE qiymatini 
# # qaytaradi ("True" so'zi ingliz tilidan "haqiqiq" yoki "to'g'ri" deb tarjima 
# # qilinadi). Aksincha, qiymatlar tenglik qanoatlantirilmasa, ifoda FALSE 
# # qiymatini qaytaradi ("False" so'zini ingliz tilidan "yolg'on" deb tarjima 
# # qilsak bo'ladi).Quyidagi misollarga e'tibor bering. Biz ism degan
# # o'zgaruvchi yaratdik, va unga 'Ali' matnini yukladik. Keling 
# # endi == yordamida ism ning qiymatini tekshirib ko'ramiz
# =============================================================================


"""MATNLARNI SOLISHTIRISH"""
# =============================================================================
# # Aksar tizimlar foydalanuvchi kiritgan matnni ma'lum bir ko'rinishga keltirib
# # oladi. Buning sababi, kompyuter uchun 'Ali', 'ALI', va 'ali' bu uchta 
# # turli hil ism. Ularni solishtirish uchun esa bir ko'rinishga
# # keltirib olish kerak.Tasavvur qiling siz yangi email manzil ochmoqchisiz, 
# # va o'zingizga yangi foydalanuvchi ismini tanlashingiz kerak. Kompyuter siz
# # kiritgan foydalanuvchi ismini tizimdagi mavjud foydalanuvchilar bilan 
# # solishtiradi va agar ism band bo'lsa sizga boshqa ism tanlashni aytadi. 
# # Solishtirish jarayonida esa, siz tanlagan ismni kichik harflarga 
# # o'tkazib, boshqa ismlar bilan solishtiradi.
# # Yuqoridagi misolda, kimdur anvar@yandex.ru manzilini band qilgan, agarda men 
# # 'Anvar', yoki 'ANvar', yoki 'ANVAR' deb login tanlasam ham, anvar@yandex.ru 
# # band bo'gani sababli men so'ragan loginlar rad qilinaveradi. 
# # Xo'sh, turli ko'rinishda yozilgan matnlarni qanday qilib solishtiramiz?
# # Juda oddiy. Matnlarni solishtirishdan avval .lower() metodi yordamida 
# # kichik harflar ko'rinishiga keltirib olamiz:
#     
#     
# ism = 'Ali'
# ism.lower() == 'ali'
# =============================================================================

    
"""QIYMATLARNING TENG EMASLIGINI TEKSHIRISH"""
# =============================================================================
# # Agar ikki qiymatning teng emasligini tekshirish talab qilinsa, 
# # != operatoridan foydalanilamiz.
# 
# 
# ism = input('ismingizni kiriting: ')
# if ism.lower() == 'ali':
#     print('Salom Ali')
#     
# else:
#     
#     print('Uzr!', ism.title(), 'biz Alini kutyapmiz' )
# =============================================================================


"""sONLARNI SOLISHTIRISH"""
# =============================================================================
# # Sonlarni solishtirishda yuqoridagi teng (==) va teng emas (!=) shartlariga
# #   qo'shimcha ravishda quyidagi mantiqiy shartlar ham qo'shiladi:
#     
# # javob = int(input("12x6 nechchiga teng?>>>>"))
# # if javob != 72:
# #     print('Javob xato')
#     
# # yosh = int(input("Yoshingiz nechida?>>>"))
# # if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
# #     print('Xush kelibsiz!')
# # else: # ask holda
# #     print('Kirish mumkin emas!')
#     
# # login = input("Yangi login tanlang:")
# # if len(login)<=5: # login uzunligini tekshiramiz
# #     print("Login 5 harfdan ko'proq bo'lishi shart!")
#     
#     
# # yil = int(input("Tug'ilgan yilingizni kiriting:"))
# # if 2020-yil<18: # foydalanuvchining yoshini hisoblaymiz
# #     print(f"Yoshingiz {2020-yil}da ekan.")
# #     print("Kirish mumkin emas!")
# # else:
# #     print("Xush kelibsiz!")
#     
#     
# # x, y = 25, 50 # x=25 va y=50
# # print("x>y") if x>y else print("x<y")
# =============================================================================


















