author = "osman cahit yüksel"
print("Toplama islemi : 1")
print("Cıkarma islemi : 2")
print("Carpma islemi : 3")
print("Bölme islemi : 4")
islem = int(input("İslem için numara seçiniz:",))
sayi1 = int(input("Sayı gir:"))
sayi2 = int(input("Sayı gir:"))
def hesap():
    return
def toplam(sayi1,sayi2):
    return sayi1+sayi2
def cıkarma(sayi1,sayi2):
    return sayi1-sayi2
def carpma (sayi1,sayi2):
    return sayi1*sayi2
def bölme (sayi1,sayi2):
    return sayi1/sayi2

if(islem==1):
    print(sayi1,"+",sayi2,"=",toplam(sayi1,sayi2))
elif(islem==2):
    print(sayi1,"-",sayi2,"=",cıkarma(sayi1,sayi2))
elif(islem==3):
    print(sayi1,"*",sayi2,"=",carpma(sayi1,sayi2))
elif(islem==4):
    print(sayi1,"/",sayi2,"=",bölme(sayi1,sayi2))
else:
    print("Böyle bir seçenek bulunmamakta")
hesap()