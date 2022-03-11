# Klavyeden AT, EV, AK ya da AL kelimeleri girildiğinde sırasıyla BEYGİR, KONUT, BEYAZ ya da KIRMIZI 
# yazan programı kodlayınız

abbrevation= str(input("Es anlamlisini istediginiz kelimeyi giriniz: "))
sozluk="Girdiginiz sozcugun es anlamlisi: "

if abbrevation== "AT": 
    print(sozluk,"BEYGİR")
elif abbrevation == "EV":
    print(sozluk,"KONUT")
elif abbrevation == "AK":   
    print(sozluk,"BEYAZ")
elif abbrevation == "AL": 
    print(sozluk,"KIRMIZI")
else:
    print("ARADIGINIZ KELIME BULUNAMADI") 