"""
23//06//2023
Dars: 9
Mavzu: For takrorlash operatori
Author: Mujibali Temiraliyev
"""


"""for BILAN TANISHAMIZ"""
# =============================================================================
#   Dasturlash davomida kodimizning biror qismini bir necha marta takrorlash
#   talab etilishi mumkin. Misol uchun, ro'yxat ichidagi har bir elementni
#   alohida qatordan konsolga chiqarish, yoki bo'lmasa har bir elementni 
#   kvdartaga oshirish va hokazo. Mana shunday vaziyatlarda bizga for operatori 
#   yordam beradi. Dasturlashda bu tsikl (loop) deb ataladi. Keling quyidagi
#   misolni ko'ramiz. Bizda mehmonlar ro'yxati bor, biz har bir mehmonning 
#   ismini yangi qatordan chiqarmoqchimiz. Buning uchun quyidagi kodni yozamiz:
# 
# mehmonlar = [ 'Ali', 'Vali', 'Hasan', 'Husan' ]
# for mehmon in mehmonlar:
#     print(mehmon)
# 
# Keling, kodni tahlil qilaylik. 
# 1-qatorda biz mehmonlar degan ro'yxat yaratdik va uni mehmonlarning ismi bilan 
# to'ldirdik.
# 2-qatorda for tsiklini bohladik. Bu qator Pythonga mehmonlar degan ro'yxatdan 
# har bir elementini olib uni yangi, mehmon degan o'zgaruvchiga yuklashni 
# buyuryapti (o'zgaruvchiga istalgan nom berishingiz mumkin. Biz tushunarli 
# bo'lishi uchun mehmon deb atadik)
# 3-qatorda biz mehmon degan o'zgaruvchining qiymatini konsolga chiqardik. 
# Bu tsikl to mehmonlar ro'yxatida elementlar tugagunga qadar takrorlanadi.
# "For" so'zi ingliz tilidan "uchun" deb tarjima qilinadi.
# Yuqoridagi kodni oddiy tilga tarjima qilsak "Mehmonlar ro'yxatidagi har bir
# mehmon uchun uning ismini konsolga chiqar" degan ma'noni beradi.
# =============================================================================


"""for QANDAY ISHLAYDI"""

# =============================================================================
# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan']
# for mehmon in mehmonlar:
#     print("Hurmatli" , mehmon, "sizni 20-dekabr kuni nahorgi oshga taklif etamiz")
#     print("Hurmat bilan Abroriddinovlar oilasi")
# =============================================================================


"""for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH"""

# =============================================================================
# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")
#     
#     
# sonlar = list(range(1,11))
# tuplam = []
# for son in sonlar:
#     tuplam.append(son**2)
# print(sonlar)
# print(tuplam)
# 
# =============================================================================


"""for va input()"""
# =============================================================================
# # for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan 
# # olingan qiymatlar bilan to'ldirish mumkin
# 
# dostlar = [] #bo'sh ro'xat yaratib olamiz
# print('5ta eng yaqin do\'stingizni ismini kiriting')
# for n in range(5):
#     dostlar.append(input(f"{n+1}, Do'stingizni ismini kriting: "))
# print(dostlar)
# =============================================================================


"""                      AMALIYOT                             """
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har 
# bir ismga takrorlanuvchi xabar yozing Yuoqirdagi tsikl tugaganidan so'ng, 
# ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod 
# necha marta takrorlanganini yozing)

# =============================================================================
# dostlar = ['ali', 'vali', 'hasan', 'husan', 'asad']
# sikl = ""
# for dost in dostlar:
#     # sikl += dost
#     print('salom', dost)
# print('sikl', len(dostlar), 'marta takrorlandi')
# =============================================================================



# =============================================================================
# #  1-100 gacha bo'lgan toq sonlar ro'xati
# toq_son = []
# for i in range(1,101,2):
#     print(i)
#     toq_son.append(i)
# print(toq_son)
# =============================================================================

    

# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1} - suhbat qilgan odamingiz kim edi? "))
# print(ismlar)









