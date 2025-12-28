print("Vücut Kitle Endeksi Hesaplama (VKI)".center(30 , " "))
kilo = float(input("kilonuzu giriniz: "))
boy = float(input("Boyunuzu giriniz: "))

VKI = (kilo/(boy/100)**2) #VKI hesaplama

if VKI < 18.5 :
    print( VKI ,"Zayıf")
elif VKI >= 18.5 and VKI <25 :
    print (VKI ,"Normal")
elif VKI >=25 and VKI <30 :
    print(VKI ,"Fazla Kilolu")
elif VKI > 30:
    print(VKI, "Obezite")