menu = int(input("Sinema biletleri için (1)  Tiyatro biletleri için (2)"))

indirim = str(input("Öğrenci misiniz? (E/H)"))
ucret = 0
if menu == 1 :
    ucret = 15
else :
    ucret = 10

if indirim.lower() == "e":
    ucret = ucret / 2
else :
    ucret = ucret

print("Ödenecek tutar :{}" .format(ucret))
    



