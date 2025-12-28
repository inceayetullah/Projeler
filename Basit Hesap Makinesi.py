print("HESAP MAKİNESİ".center(30 , " "))

sayi1 =float(input("Bir sayı gir : "))
sayi2 =float(input("Bir sayı gir : "))

islem = input("Toplama (+) , Çıkarma (-) , Çarpma (x) , Bölme (/)")


if islem == "+" :
   
   print(sayi1 + sayi2)

elif islem == "-" :
   
   print(sayi1 - sayi2)

elif islem == "x" :
   
   print(sayi1 * sayi2)
   
elif islem == "/" : 
   
   print(sayi1 / sayi2)

else :
   
   print("Yanlış argüman girdisi")
   
