"""
22//06//2023
Dars: 5
Mavzu: Matnlar bilan ishlash (STRING)
Author: Mujibali Temiraliyev
"""





# =============================================================================
# # ism = 'Cristiano'
# # familiya = 'Ronaldo'
# # ism_familiya = (ism + ' ' + familiya) #Matnlarni qo'shish uchun + operatoridan foydalanmiz
# # print(ism_familiya)
# # print("Mening ismim " + ism)
# =============================================================================



# =============================================================================
# #f-string
# # Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish uchun 
# # f-string usulidan  f"{matn1} {matn2}" ham foydalansak bo'ladi
# # ism = 'Cristiano'
# # familiya = 'Ronaldo'
# # ism_familiya = f"{ism} {familiya}"
# # print(ism_familiya)
# =============================================================================




# =============================================================================
# # Bu usul yordamida uzun matnlarni ham yasash mumkin:   
# # ism = "Cristiano"
# # familiya = 'Ronaldo'
# # print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")
# =============================================================================



# =============================================================================
# #Maxsus belgilar:
# # Matnga bo'shliq qo'shish uchun \t belgisidan, 
# # yangi qatordan boshlash uchun \n belgisidan foydalanamiz
# # print('hello \tworld!') # \t bo'shliq qo'shadi
# # print('hello \nworld!') # \n yangi qatordan yozadi
# =============================================================================

    


# =============================================================================
# # Pythonda string ustida amalga oshirish mumkin bo'lgan tayyor amallar to'plami mavjud. 
# # Bunday amallar to'plami metodlar deb ataladi. 
# # Metodlarni qo'llash uchun metod nomi matndan so'ng .metod_nomi() ko'rinishida yoziladi. 
# # Keling shunday metodlarning ba'zilari bilan tanishaylik.
# # upper() va lower() metodlari
# # ism = 'ahmad'
# # print('Mening ismim ' + ism.upper())  # upper() metodi matndagi har bir harfni katta harfga o'zgartiradi.
# # print('Mening ismim ' + ism.lower())  #lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.
# =============================================================================


# =============================================================================
# # # title() va capitalize() metodlari
# # ism = 'ahmad'
# # print(ism.title())        #title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.
# # print(ism.capitalize())   #capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.
# =============================================================================



# =============================================================================
# # strip(), rstrip() va lstrip() metodlari
# # Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi
# # ism = '   Ahmad   '
# # familiya = 'Qosimov'
# # print('Mening ismim ' + ism + ' Familiyam ' + familiya)           #asl ko'risnishi
# # print('Mening ismim ' + ism.lstrip() + ' Familiyam ' + familiya)  #lstrip() — matn boshidagi bo'shliqni olib tashlaydi
# # print('Mening ismim ' + ism.rstrip() + ' Familiyam ' + familiya)  #rstrip() — matn oxiridagi bo'shliqni olib tashlaydi
# # print('Mening ismim ' + ism.strip() + ' Familiyam ' + familiya)   #strip() — matn oxiridagi bo'shliqni olib tashlaydi# strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
# =============================================================================





# =============================================================================
# # INPUT —FOYDALANUVCHI BILAN MULOQOT
# # Shu paytgacha biz o'zgaruvchilarning qiymatini dasturning ichida berayotgan edik. 
# # Keling endi qiymatni o'zimiz emas, balki dastur foydalanuvchilariga kiritish imkonini beramiz. 
# # Buning uchun input() funktsyasidan foydalanamiz. 
# # ism = input('ismingizni kiriting: \n>>>')
# # print('Mening ismim ' + ism.title())
# =============================================================================




# =============================================================================
# #                   Amaliyot
# 
# # kocha = "Bog'bon"
# # mahalla = "Sog'bon"
# # tuman = "Bodomzor"
# # viloyat = "Samarqand"
# 
# # # Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# # # Diqqat uzun kodlarni \ belgisi yordamida keyingi qatorga
# # # ko'chirish mumkin
# # print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
# #       tuman + " tumani, " + viloyat + " viloyati")
# 
# # #Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
# # print("Iltimos, quyidagi ma'lumotlarni kiriting:")
# # kocha = input("Ko'changiz: ")
# # mahalla = input("Mahallangiz: ")
# # tuman = input("Tumaningiz: ")
# # viloyat = input("Viloyatingiz: ")
# # print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
# #       tuman + " tumani, " + viloyat + " viloyati")   
# 
# # # Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing
# # print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
# #       tuman + " tumani,\n" + viloyat + " viloyati")
# 
# # # Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
# # manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# # print(manzil)
# 
# # #manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.
# # print(manzil.upper())
# # print(manzil.lower())
# # print(manzil.title())
# # print(manzil.capitalize())
# =============================================================================











