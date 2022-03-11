# Klavyeden 212, 312, 216 ve 352 kodları girildiğinde sırasıyla 
# İSTANBUL AVRUPA, ANKARA, İSTANBUL ANADOLU ve KAYSERİ yazan programı kodlayınız

variable1 = int(input("Lutfen istediginiz sehrin alan kodunu giriniz: "))
sozluk="Alan kodunu girdiginiz sehir :"

if variable1 == 212:
    print(sozluk,"İSTANBUL AVRUPA") 
elif variable1 == 312:
    print(sozluk, "ANKARA")
elif variable1 == 216:
    print(sozluk, "İSTANBUL ANADOLU")
elif variable1 == 352:
    print(sozluk, "KAYSERİ")
else:
    print("ARADIGINIZ KELIME BULUNAMADI")             