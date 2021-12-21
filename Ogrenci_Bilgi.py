ogrenciler = {}
numara = input(("öğrenci numarası gir:"))
isim = input(("öğrenci isim: "))
soyisim = input(("öğrenci soyisim: "))
telefon = input(("öğrenci telefon:"))

ogrenciler[numara]= {
    'isim' : isim,
    'soyisim' : soyisim,
    'telefon' : telefon,
}
print(ogrenciler)
