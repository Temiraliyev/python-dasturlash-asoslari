"""
24//09//2023
Dars: 20
Mavzu: FUNCTIONS (funksiyalar)dan qiymat qaytarish
Author: Mujibali Temiraliyev
"""


# =============================================================================
# def toliq_ism_yasa(ism ,familiya):
#     """toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     print(toliq_ism)
# toliq_ism_yasa("olim", "olimov")
# =============================================================================

# =============================================================================
# def toliq_ism_yasa(ism ,familiya):
#     """toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism
# talaba = toliq_ism_yasa("olim", "olimov")
# talaba1 = toliq_ism_yasa("hakim", "olimov")
# talaba2 = toliq_ism_yasa("olim", "hakimov")
# print(f"{talaba1} va {talaba2} darsga kelmadi ")
# =============================================================================



# =============================================================================
# def toliq_ism_qaytaruvchi(ism, familiya, otasining_ismi=''):
#     """Toliq ism qaytaruvchi funksiyA"""
#     if otasining_ismi:
#         toliq_ismi = f"{ism} {otasining_ismi} {familiya} "
#         
#     else:
#         toliq_ismi = f"{ism} {familiya}"
#     return toliq_ismi.title()
# talaba1 = toliq_ism_qaytaruvchi("sardor", "mamadaliyev", "tairovich")
# talaba2 = toliq_ism_qaytaruvchi("sardor", "sanginov")
# print(f"{talaba1} {talaba2}")
# =============================================================================
        
        
# =============================================================================
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto    
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
# =============================================================================


# =============================================================================
# def oraliq(min,max):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# 
# print(oraliq(0,10))
# print(oraliq(10,21))
# =============================================================================

# =============================================================================
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting ",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
# 
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# =============================================================================
    
