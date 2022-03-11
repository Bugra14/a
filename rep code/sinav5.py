# Klavyeden TOY, LOSE, SOFT ve FAT kelimeleri girildiğinde sırasıyla 
# OYUNCAK, KAYBETMEK, YUMUŞAK ve ŞİŞMAN yazan programı kodlayınız

diffLang = str(input("Lutfen Türkçesini istediginiz kelimeyi giriniz:"))
sozluk= "Ingilizce olarak girdiginiz kelimenin turkcesi: "

if diffLang == "TOY":
    print("OYUNCAK") 
elif diffLang == "LOSE":
    print("KAYBETMEK")
elif diffLang == "SOFT":
    print("YUMUŞAK")
elif diffLang == "FAT":
    print("ŞİŞMAN")
else:
    print("ARADIGINIZ KELIME BULUNAMADI")  