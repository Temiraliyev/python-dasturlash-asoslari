"""
22//06//2023
Dars: 8
Mavzu: Ro'yxatlar  bilan ishlash
Author: Mujibali Temiraliyev
"""


"""RO'YXATNI TARTIBLASH"""
# =============================================================================
# # Aksar holatlarda ro'yxat ichidagi elementlarni alifbo ketma-ketligida 
# # tartiblash talab qilinishi mumkin. Buning uchun list uchun maxsus .sort() 
# # metodidan foydalanamiz.
# 
# # cars = ['malibu', 'captiva', 'audi', 'gentra', 'lacetti', 'cobalt', 'damas', 'matiz']
# # cars.sort()
# # print(cars)
# # cars.sort(reverse=True) # 'reverse=True' tezkari tartiblash
# # print(cars)
#                   # """.sorted()"""
# # cars = ['malibu', 'captiva', 'audi', 'gentra', 'lacetti', 'cobalt', 'damas', 'matiz']
# # print(sorted(cars))   
# # print(sorted(cars ,reverse=True))  #teskari tartiblash
# =============================================================================


"""RO'YXATNI AYLANTIRISH"""
# =============================================================================
# # Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab
# # qilinishi mumkin. Buning uchun .reverse() metodidan foydalanamiz.
# 
# # fruits = ['pear','banana','apple','watermelon','lemon']
# # fruits.reverse()
# # print(fruits)
# =============================================================================


"""RO'YXATNING UZUNLIGINI BILISH"""
# =============================================================================
# # Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun
# #  len() funktsiyasidan foydalanamiz
# 
# # fruits = ['pear','banana','apple','watermelon','lemon']
# # print('Elementlar soni:', len(fruits), 'ta')
# =============================================================================

"""range() FUNKTSIYASI"""
# =============================================================================
# # Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini 
# # yaratishimiz mumkin. list() funktsiyasi yordamida esa bu oraliqni ro'yxat 
# # shaklida saqlab olamiz
# 
# # sonlar = list(range(0,10)) 
# # print(sonlar)
# 
# 
# #                 ESLATMA
# # Diqqat! E'tibor qiling range() funktsiyasi ikkinchi indeksdan bitta avval 
# # to'xtaydi. range() yordamida qadamni ham berishimiz mumkin
# 
# 
# # juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# # toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# # print("Juft sonlar: ", juft_sonlar)
# # print("Toq sonlar: ", toq_sonlar)
# =============================================================================


"""SONLI RO'YXAT USTIDA SODDA AMALLAR"""
# =============================================================================
# # Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham bajarish mumkin. 
# # Misol uchun ro'yxatdagi eng kichik sonni topish uchun min() funktsiyasidan, 
# # eng katta sonni topish uchun esa max() funktsiyasidan, sonlarning yig'indisini
# # topish uchun esa sum() funktsyasidan foydalansak bo'ladi
# 
# # narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# # arzon = min(narhlar)
# # qimmat = max(narhlar)
# # jami = sum(narhlar)
# # print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)
# =============================================================================


"""RO'YXATNI KESISH"""
# =============================================================================
# # Ba'zida ro'yxatning ma'lum bir bo'lagini ajratib olish talab qilinishi mumkin,
# # deylik biz quyidagi cars degan ro'yxatdan birinchi 3 ta elementni ajratib 
# # olmoqchimiz, buning uchun biz boshlang'ich va oxirgi indekslarni beramiz
# 
# # cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# # my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# # print(my_cars) 
# # print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# # print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi
# =============================================================================


"""RO'YXATDAN NUSXA OLISH"""

# =============================================================================
# # sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# # sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
# # sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# # sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# # print("Bu sonlar ro'yxati:", sonlar)
# # print("Bu sonlar2 ro'yxati:", sonlar2)
# =============================================================================


"""TUPLES - O'ZGARMAS RO'YXAT"""
# =============================================================================
# # Dastur yaratish davomida o'zgarmas ro'yxat tuzish talab qilinishi mumkin.
# # Pythonda bunday ro'yxatlar tuples deb yuritiladi. Tuple ichidagi qiymatlarni
# # bir marta, dastur boshida beriladi va so'ngra o'zgartirib bo'lmaydi. 
# # List dan farqli ravishda, Tuple e'lon qilishda kvadrat qavslar [] o'rniga
# # oddiy qavslar () ishlatiladi
# # tomonlar = (20, 30, 55.2)
# # print(tomonlar)
# 
# # toys = ('bus','car','bear','dino','snake','lizard')
# # print(toys[0])
# # print(toys[-1])
# # print(toys[2:5])
# 
# # toys = ('bus','car','bear','dino','snake','lizard')
# # toys[3] = 'dragon'
# # Demak yuqorida ko'rib turganingiz kabi, bu operatsiya xatolikka olib keldi. 
# # Shu kabi ro'yxatdan biror elementni o'chirish yoki yangi element qo'shish 
# # ham mumkin emas. Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li 
# # o'zgarmas ro'yxatni list() funktsiyasi yordamida List (oddiy ro'yxat) 
# # ko'rinishiga keltirib olish, o'zgarishlarni bajarsih va qaytarib tuple() 
# # funktsiyasi yordamida o'zgarmas ro'yxatga o'tkazish mumkin
# 
# # toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# # toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # # Ro'yxatga o'zgartirishlar kiritamiz
# # toys.append('dragon')
# # toys.remove('bus')
# # toys[1] = 'mcqueen'
# # toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# # print(toys)
# =============================================================================



# =============================================================================
# """Amaliyot"""
# #O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# davlatlar = ["O'zbekiston","Qozog'iston", "Rossiya", "Malayziya", "Singapur", "AQSh"]
# print(davlatlar)
# 
# #Ro'yxatning uzunligini konsolga chiqaring
# print(len(davlatlar))
# 
# #sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(davlatlar))
# 
# #sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(sorted(davlatlar, reverse=True))
# 
# #Asl ro'yxatni qaytadan konsolga chiqaring
# print(davlatlar)
# 
# #reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print(davlatlar)
# 
# #sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)
# 
# #120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# sonlar = list(range(120,1200))
# 
# #Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print(sum(sonlar))
# 
# #Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# print(max(sonlar)-min(sonlar))
# 
# #Ro'yxatdagi elementlar sonini hisoblang
# print(len(sonlar))
# 
# #Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# print(sonlar[:20])
# print(sonlar[-20:])
# print(sonlar[530:550])
# 
# #taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# taomlar = ['osh','somsa','norin','shashlik','qozonkabob']
# 
# #nonushta degan yangi ro'yxatga taomlardan nusxa oling
# nonushta = taomlar[:]
# 
# #Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
# nonushta.remove('norin')
# nonushta.remove('shashlik')
# nonushta.remove('qozonkabob')
# nonushta.append('non va qaymoq')
# nonushta.append('issiq non')
# 
# #Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# print(taomlar)
# print(nonushta)
# 
# #Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
# nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non"
# =============================================================================











