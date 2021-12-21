ogrenci_user = "osman"
ogrenci_pass = "12345"
username = input("Username giriniz: ")
password = int(input("Password giriniz: "))
if(username==ogrenci_user):
    print("Username doğru")
elif(password==ogrenci_pass):
    print("Giriş başarılı")
else:
    print("Username veya password yanlış")

