"""
26//06//2023
Dars: 15
Mavzu: Lug'atlar bilan ishlaymiz
Author: Mujibali Temiraliyev
"""


# =============================================================================
# .items()
# telefonlar = {
#     'ali': "iphone x",
#     'vali': "iphone 12",
#     'hasan': "galaxy s21",
#     'husan': "galaxy a54"
#     }
# print(telefonlar.items())
# =============================================================================


# =============================================================================
# telefonlar = {
#     'ali': "iphone x",
#     'vali': "iphone 12",
#     'hasan': "galaxy s21",
#     'husan': "galaxy a54"
#     }
# for kalit, qiymat in telefonlar.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}")
# =============================================================================



# =============================================================================
# telefonlar = {
#     'ali': "iphone x",
#     'vali': "iphone 12",
#     'hasan': "galaxy s21",
#     'husan': "galaxy a54"
#     }
# for k, q in telefonlar.items():
#     print(f"{k.title()} ning telefoni {q}")
# =============================================================================


# =============================================================================
# # .keys()  kalit
# telefonlar = {
#     'ali': "iphone x",
#     'vali': "iphone 12",
#     'hasan': "galaxy s21",
#     'husan': "galaxy a54"
#     }
# for tel in telefonlar.keys():
#     print(tel.title())
# print(telefonlar.keys())
# =============================================================================



# =============================================================================
# #.values()   qiymat
# 
# telefonlar = {
#     'ali': "iphone x",
#     'vali': "iphone 12",
#     'hasan': "galaxy s21",
#     'husan': "galaxy a54"
#     }
# for tel in telefonlar.values():
#     print(tel.title())
# print(telefonlar.values())
# =============================================================================



# =============================================================================
# # set() lug'atda takrorlangan qiymatni faqat 1 tasini chiqaradi
# telefonlar = {
#     'ali': "iphone x",
#     'vali': "iphone 12",
#     'hasan': "galaxy s21",
#     'husan': "galaxy a54",
#     'sardor': "galaxy a54",
#     'sarvar': "iphone 12"
#     }
# for tel in set(telefonlar.values()):
#     print(tel.title())
# =============================================================================



# =============================================================================
# #                               Amaliyot
# mahsulotlar = {'olma': 10000, 'gilos': 6000, 'shaftoli': 3000, 'anor': 15000}
# bozorlik = ['olma', 'banan', 'olcha', 'o\'rik', 'shaftoli']
# for mahsulot in mahsulotlar.keys():
#     # print(mahsulot.title())
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#     else:
#         print(f" Kechirasiz '{mahsulot.title()}' bizda mavjud emas")
# =============================================================================


# =============================================================================
# #                                   Amaliyot
# telefonlar = {'a32': 1_600_000, 'iphone_x': 3_000_000, 's21': 2_000_000}
# telefon = ['a32']
# for mahsulot in telefonlar:
#     if mahsulot in telefon:
#         print(f"{mahsulot.title()} mavjud. Narxi: {telefonlar[mahsulot]} so'm")
#     else:
#         print(f"Kechirasiz, {mahsulot.title()} modelidagi telefon mavjud emas!")
# =============================================================================


























