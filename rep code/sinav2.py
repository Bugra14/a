# Klavyeden İTÜ, YTÜ, ODTÜ ya da ERÜ kısaltmaları girildiğinde sırasıyla İSTANBUL TEKNİK ÜNİVERSİTESİ, 
# YILDIZ TEKNİK ÜNİVERSİTESİ, ORTADOĞU TEKNİK ÜNİVERSİTESİ ya da ERCİYES ÜNİVERSİTESİ yazan programı kodlayınız

abbreviation = str(input("Lutfen acilim halinde istedigniz universitenin kisaltmasini giriniz:"))
sozluk="Girdiginiz kisaltmanin acilimi :"

if abbreviation == "İTÜ":
    print(sozluk ,"İSTANBUL TEKNİK ÜNİVERSİTESİ")
elif abbreviation == "YTÜ":
    print(sozluk, "YILDIZ TEKNİK ÜNİVERSİTESİ")
elif abbreviation == "ODTÜ":
    print(sozluk,"ORTADOĞU TEKNİK ÜNİVERSİTESİ")
elif abbreviation == "ERÜ":
    print(sozluk, "ERCİYES ÜNİVERSİTESİ")
else:
    print("Aradiginiz kelime bulunamadi")      