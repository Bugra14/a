# Klavyeden FB, GS, BJK ya da KS kısaltmaları girildiğinde sırasıyla FENERBAHÇE, GALATASARAY, 
# BEŞİKTAŞ ya da KAYSERİSPOR, farklı harfler girildiğinde “ARADIĞINIZ TAKIM BULUNAMADI” yazan programı kodlayınız

abbreviation = str(input("Acilmis halini istediginiz takimin kisaltilmis halini giriniz: "))
sozluk="Girdiginiz kisaltmanin acilimi :"

if abbreviation == "FB":
    print(sozluk,"FENERBAHCE")  
elif abbreviation == "GS":
    print(sozluk, "GALATASARAY")    
elif abbreviation == "BJK":
    print(sozluk ,"BESIKTAS")
elif abbreviation == "KS":
    print(sozluk, "KAYSERISPOR")
else:
    print("ARADIGINIZ TAKIM BULUNAMADI")        