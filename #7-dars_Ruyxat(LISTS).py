"""
22//06//2023
Dars: 7
Mavzu: Ro'yxatlar  (LISTS)
Author: Mujibali Temiraliyev
"""


"""LIST BILAN TANISHAMIZ"""
# =============================================================================
# # Avvalgi darsimizda biz o'zgaruvchi yaratish, va uning ichida biror qiymatni (matn yoki son) saqlashni o'rgandik. Bunda biz bitta o'zgaruvchiga bitta qiymat berdik xolos. 
# # Bugun o'rganadigan navbatdagi mal'umot turi List (ro'yxat) deb ataladi. Ro'yxat o'z nomi bilan, bitta o'zgaruvchida bir nechta qiymatlarni saqlash imkonini beradi. Bu qiymatlar List elementlari deyiladi. Ro'yxatda son, matn yoki aralash turdagi elementlarni saqlash mumkin. 
# # List quyidagicha yaratiladi:
# # mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# # narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# # sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# # ismlar = [] # bo'sh ro'yxat
# # print(sonlar)
# =============================================================================


"""LIST ELEMENTLARI"""
# =============================================================================
# # Ro'yxatdagi har bir element tartib bilan joylashgani sababli, biz istalgan 
# # elementga uning tartib raqami (indeksi) bo'yicha murojat qilishimiz mumkin. 
# # Dasturlash olamida indeks 0 dan boshlanadi! Ya'ni Listning birinchi 
# # elementing tartib raqami (indeksi) 0 ga, ikkinchi elementning 
# # indeksi 1 ga teng va hokazo.
# # mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# # print("Birinchi meva: ", mevalar[0].upper())
# # print("Ikkinchi meva: ", mevalar[1])
# # narhlar = [12000, 18000, 10900, 22000]
# # print(narhlar[2] + narhlar[3])
# 
# # Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat 
# # qilish mumkin. Bu usul Listning uzunligini bilmaganda juda asqotadi.
# # car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Oxirgisi']
# # print(car_models[-7]) # Listning eng oxirgi 
# # # elementiga -1 bilan murojat qilamiz 
# =============================================================================


"""ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH"""
# =============================================================================
# # Dastur davomida listning tarkibi o'zgarishi, yangi elementlar qo'shilishi,
# # da'zi elementlar o'chirilishi tabiiy hol. Misol uchun "Bozorlik ro'yxati" 
# # degan dasturni tasavvur qilaylik, foydalanuvchi ro'yxatga yangi 
# # mahsulotlar qo'shishi, sotib olganlarini esa o'chrishi mumkin. 
# # Elementni o'zgartirishRo'yxatdagi biror elementning qiymatini o'zgartirish 
# # uchun, o'sha elementga indeksi bo'yicha murojat qilamiz 
# # va yangi qiymat yuklaymiz
# 
# # narxlar= [10200, 13000, 61000 ]
# # print(narxlar)
# # narxlar[0] = 5000 #ro'yxatimizdagi 0-element o'zgartirildi
# # narxlar[2] = narxlar[2] + 100000
# # print(narxlar[0])
# # print(narxlar[2])
# =============================================================================


"""Yangi element qo'shish"""
# =============================================================================
# # .append() metodi
# # Ro'yxatga yangi element qo'shishning oson usuli bu .append() metodi yordamida 
# # ro'yxatning oxiriga qiymat qo'shish:
# # cars = [] # bo'sh ro'yxat yaratamiz
# # cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# # cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# # cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# # print(cars)
# # cars1 = ['Lacetti ', 'Nexia ', 'Cobalt' ]
# # print(cars1)
# # cars1.append('Spark '  + 'Damas')
# # print(cars1)
# =============================================================================


""".insert() metodi"""
# =============================================================================
# # Ro'yxatning istalgan joyiga yangi element qo'shish uchun 
# # .insert() metodidan foydalanamiz. .insert() metodi ichida 
# # yangi elementning indeksi va qiymati beriladi
# # cars = [] # bo'sh ro'yxat yaratamiz
# # cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# # cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# # cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# # print(cars)
# # cars1 = ['Lacetti ', 'Nexia ', 'Cobalt' ]
# # print(cars1)
# # cars1.insert(0, 'Gentra')
# # print(cars1)
# =============================================================================


"""Elementni o'chirish"""
# =============================================================================
# # Ro'yxatdan biror elementni olib tashlash uchun uning indeksini yoki 
# # qiymatini bilishimiz lozim. Inedks yordamida olib tashlash uchun 
# # del operatoridan foydalanamiz.
# # cars = []
# # cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# # cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# # cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# # print(cars)
# # cars1 = ['Lacetti ', 'Nexia ', 'Cobalt' ]
# # print(cars1)
# # cars1.insert(0, 'Gentra')
# # print(cars1)
# # del cars1[2]
# # print(cars1)
# =============================================================================


""".remove(qiymat)"""
# =============================================================================
# # Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan 
# # foydalanamiz. Buning uchun qavs ichida o'chirib tashlash kerak 
# # bo'lgan qiymatni yozamiz
# # mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# # print(mevalar)
# # mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
# # print(mevalar)
# =============================================================================


"""Elementni sug'urib olish"""
# =============================================================================
# # Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni 
# # ro'yxatdan sug'urib olish va undan foydalanish talab qilinishi mumkin.
# #  Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.
# # bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# # mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
# # print("Men " + mahsulot + " sotib oldim")
# # print("Olinmagan mahsulotlar: ", bozorlik)
# =============================================================================
