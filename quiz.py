soru1 = "1.SORU ==> İstiklal marşının yazarı kimdir?"
soru2 = "2.SORU ==> Organik maddeler hangi atomlardan oluşmaktadır?"
soru3 = "3.SORU ==> Cos 60 kaçtır?"
soru4 = "4.SORU ==> Ülkemizin yüz ölçümü bakımından en büyük şehri hangisidir?"  
dogru = "Doğru Cevap Tebrikler "
yanlıs = "Yanlış Cevap"
print("________________________________")   

isim = input("İsim Soyisim => ")
print("Hoşgeldin "+isim)

print("________________________________")   

print(soru1)
print("A-) Mehmet Akif Ersoy")
print("B-) Mustafa Kemal Atatürk")
print("C-) Nene Hatun")
print("D-) Osman Paşa")
cevap1 = input("Cevap = ")
if(cevap1 == "A" or cevap1 == "a"):
    print(dogru) 
elif(cevap1 == "B" or cevap1 == "b" or cevap1 == "C" or cevap1 == "c" or cevap1 == "D" or cevap1 == "d"):
    print(yanlıs)
else:
    print("Böyle bir şık yok")
print("________________________________")   

print(soru2)
print("A-) Yapısında C,O ve Li bulunan atomlardır.")
print("B-) Yapısında C,Mn ve K bulunan atomlardır.")
print("C-) Yapısında Co,K ve Pb bulunan atomlardır.")
print("D-) Yapısında C,O ve N bulunan atomlardır.")
cevap2 = input("Cevap = ")
if(cevap2 == "D" or cevap2 == "d"):
    print(dogru) 
elif(cevap2 == "A" or cevap2== "a" or cevap2 == "B" or cevap2 == "b" or cevap2 == "C" or cevap2 == "c"):
    print(yanlıs)
else:
    print("Böyle bir şık yok")
print("________________________________")  

print(soru3)
print("A-) 5 bölü 2")
print("B-) 4 bölü 2")
print("C-) 1 bölü 2")
print("D-) 2 bölü 2")
cevap3 = input("Cevap = ")
if(cevap3 == "C" or cevap3 == "c"):
    print(dogru)
elif(cevap3 == "A" or "a" or cevap3 == "B" or cevap3 =="b" or cevap3 == "D" or cevap3 == "d"):
    print(yanlıs)
else:
    print("Böyle bir şık yok")
print("________________________________")  

print(soru4)
print("A-) Manisa")
print("B-) Konya")
print("C-) İstanbul")
print("D-) Ankara")
cevap4 = input("Cevap = ")
if(cevap4 == "B" or  cevap4 == "b"):
    print(dogru)
elif(cevap4 == "A" or cevap4 == "a" or cevap4 == "C" or cevap4 == "c" or cevap4 == "D" or cevap4 == "d"):
    print(yanlıs)
else:
    print("Böyle bir şık yok")
































