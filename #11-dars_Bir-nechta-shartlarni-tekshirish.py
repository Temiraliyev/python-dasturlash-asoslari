"""
24//06//2023
Dars: 11
Mavzu: Bir nechta shartlarni tekshirish
Author: Mujibali Temiraliyev
"""


"""if-elif-else KETMA-KETLIGI"""

# Dastur davomida bir nechta shartni tekshirish talab qilinishi mumkin. 
# Bunday holatda biz if-elif-else ketma-ketligidan foydalanamiz. 
# elif - else va if so'zalrining jamlanmasi bo'lib, "aks holda, agar" 
# deb tarjima qilinadi. Bunday if bilan boshlangan ketma-ketlik bir nechta 
# elif lardan iborat bo'lishi mumkin. 
# Python avval if shartini tekshiradi, shart bajarilmasa elif ga o'tadi,
# birinchi elif sharti bajarilmasa keyingi elif ga o'tadi va hokazo 
# davom etaveradi.
# Diqqat!if-elif-else ketma-ketlikda biror shart bajarilishi bilan,
# Python qolgan shartlarni tekshirmaydi.
# Keling bir misol ko'ramiz. Hayvonot bo'giga kirish quyidagicha belgilangan:
# 4 yoshdan kichik bolalarga kirish bepul
# 4 yoshdan 12 yoshgacha kirish 5000 so'm
# 12 yoshdan kattalarga 10000 so'm
# Foydalanuvchidan yoshini so'rab, hayvonot bog'iga kirish chiptasi narhini 
# chiqaruvchi dastur yozamiz.


# =============================================================================
# yosh = int(input('Yoshingiz nechida?>>> '))
# if yosh <= 0:
#     print('notug\'ri son kiritdingiz!')
# else:
#     if yosh <= 4:
#         print('sizga kirish bepul')
#     elif yosh <= 12:
#         print('sizga kirish 5000 so\'m')
#     else:
#         print('kirish 10 000 so\'m')
# =============================================================================

                                    # """ESLATMA"""
# Kod yozishda yaxshi amaliyotlardan biri, kodlarni qisqa yozish va 
# buyruqlarni qayta-qayta takrorlamaslik. Bu kelajakda kodni o'zgartirishda 
# ham juda qo'l keladi. 


# =============================================================================
# yosh = int(input('Yoshingiz nechida?>>> '))
# if yosh <= 0:
#     print('notug\'ri son kiritdingiz!')
# else:
#     if yosh <= 4:
#         narx = 0
#     elif yosh <= 12:
#         narx = 5000
#     else:
#         narx = 10000
#     print(f"Sizga kirish {narx} ming so'm")
# =============================================================================


# Avval aytganimizdek,  if-elif-else zanjirida bit nechta elif lar 
# bo'lishi mumkin. Misol uchun, hayvonot bog'i qariyalar uchun chegirma
#  e'lon qilsa, kodimizni quyidagicha o'zgartirishimiz mumkin

# =============================================================================
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4: # yosh bolalarga bepul
#     price = 0
# elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
#     price = 5000
# elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#     price = 10000
# else: # qariyalarga esa 8000 so'm
#     price = 8000
# print(f"Sizga kirish {price} so'm")
# =============================================================================


                           # """"AND, OR OPERATORLARI""""
# Yuqorida aytganimizdek, if-elif-else zanjirida shartlarning biri bajarilishi 
# bilan, Python qolgan shartlarni tekshirmaydi va ularni bajarmaydi. Lekin 
# ba'zida biz 2 yoki undan ko'p shartlarni tekshirishni talab qilishimiz 
# mumkin, buing uchun AND va OR operatorlaridan foydalanamiz.
                            # """OR OPERATORI"""
# OR ingliz tilidan "yoki" deb tarjima qilinadi, va ikki va undan ko'p 
# shartlardan biri bajarilishini tekshirishda ishlatiladi. Quyidagi misolni 
# ko'raylik, foydalanuvchidan hafta kunini so'raymiz va agar kun shanba yoki
# yakshanba bo'lsa, bugun dam olish kuni degan xabarni chiqaramiz, aks holda
# bugun ish kuni degan xabarni chiqaramiz

# =============================================================================
# kun = input('Hafta kunini kiriting: >>>')
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('bugun dam olish kuni')
# else:
#     print('bugun ish kuni')
# =============================================================================


#                           """AND OPERATORI"""
# AND ingliz tilidan "va" deb tarjima qilinadi, va ikki va undan ko'p 
# shartlarning barchasi bajarilishini tekshirishda ishlatiladi. 
# AND operatori bilan yozilgan shartlarning barchasi bajarilgandagina
# TRUE qiymati qaytadi, agar shartlardan biri bajarilmay qolsa ham 
# FALSE qiymati qaytadi.
# Quyidagi misolni ko'ramiz


# =============================================================================
# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")
# =============================================================================


# BOOLEAN MA'LUMOTLAR TURI
# Avvalgi darsimizda biz turli ifodalarni solishtirishda TRUE yoki FALSE 
# qiymatlari qaytishini ko'rdik. Bu qiymatlar boolean (mantiqiy) qiymatlar 
# deb ataladi, va dasturlashda juda keng qo'llaniladi. Pythonda 
# o'zgaruvchilarda boolean qiymatlarni ham saqlash mumkin. 
# Quyidagi dasturga e'tibor bering. Deylik, restoranimizga kelgan mijoz 
# 15000 so'mlik taom oldi, biz mijoz qo'shimcha choy va salat ham 
# olgan (olmaganiga) qarab ularning narhini ham  yakuniy narhga
# qo'shishimiz kerak. Mijozning choy yoki salat olgan (olmaganini) biz
# TRUE va FALSE qiymatlari bilan belgiladik.

# =============================================================================
# narh = 15000 # mijoz 15000 so'mga taom oldi.
# choy = True # mijoz choy ham oldi
# salat = False # mijoz salat olmadi
# 
# if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#     narh = narh + 10000 # narhga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#     narh = narh + 5000 # narhga 5000 so'm qo'shamiz
# 
# print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz
# =============================================================================


# SHARTLARNI KETMA-KET TEKSHIRISH
# if-elif-else zanjirining kamchiligidan biri, shartlardan biri bajarilishi 
# bilan, qolgan shartlar tekshirilmaydi. Shung uchun ba'zida shartlarni 
# ketma ket tekshirish uchun, har bir shartni alohida if bilan ajratish 
# talab qilinishi mumkin.
# Yuqoridagi misolni kengaytiraylik

# =============================================================================
# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# #Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:   # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:    # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti: # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
#     
# print(f"Jami {narh} so'm")
# =============================================================================


# RO'YXAT TARKIBINI TEKSHIRISH
# in OPERATORI
# in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element
#  borligini tekshirishimiz mumkin.


# =============================================================================
# menu = ['osh', 'manti', 'xotdog', 'shurva']
# zakaz = input('nima ovqat yeysiz?>>>\n')
# if zakaz.lower() in menu:
#     print('buyurtma qabul qilindi')
# else:
#     print('kechirasiz bizda bunday ovqat yo\'q')
# =============================================================================


# not in OPERATORI

# =============================================================================
# menu = ['osh', 'manti', 'xotdog', 'shurva']
# zakaz = input('nima ovqat yeysiz?>>>\n')
# if zakaz.lower() not in menu:
#     print('kechirasiz bizda bunday ovqat yo\'q')
# else:
#     print('buyurtma qabul qilindi')
# =============================================================================


# IKKI RO'YXATNI SOLISHTIRISH
# Ikki ro'yxatning tarkibi quyidagicha tekshiriladi

# =============================================================================
# menu = ['osh', 'manti', 'kabob']
# buyurtma = ['lagmon', 'manti', 'lavash']
# for bor in menu:
#     if bor in buyurtma:
#         print(f"Menuda {bor} bor")
#     else:
#         print('kechirasiz menuda bunaqa taom yo\'q')
# =============================================================================
        

#                  RO'YXAT BO'SH EMASLIGINI TEKSHIRISH
# Yuqoridagi dasturimizda biz foydalanuvchi buyurtma 
# berdi deb tasavvur qilyapmiz. Lekin foydalanuvchidan 
# bo'sh ro'yxat kelsachi? Demak for tsiklini bajarishdan
# avval ro'yxat bo'sh emasligiga amin bo'lishimiz kerak. 
# Buning uchun avvalgi kodimizni quyidagicha o'zgartiramiz



# =============================================================================
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]
# 
# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")
# =============================================================================

                 # AMALIYOT

# =============================================================================
# b_son = int(input('1-sonni kiriting: \n'))
# i_son = int(input('2-sonni kiriting: \n'))
# 
# if b_son>i_son:
#     print(f"{b_son} > {i_son}")
# else:
#     print(f"{b_son} < {i_son}")
# =============================================================================


  


































































