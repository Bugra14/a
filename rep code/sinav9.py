# Klavyeden girilen 5 sayıdan pozitif olanları toplayan programı for döngüsü kullanarak kodlayınız. 
#Test edilecek sayılar 6, -5, -13, 12, 4 ve sonuç 22 çıkacaktır

toplam=0

for i in range(0,5):
    pozitifSayi= int(input("Toplanacak sayilardan {}. sayiyi giriniz: ".format(i+1)))
    
    if pozitifSayi>0:
        toplam= toplam + pozitifSayi
        i=i+1
    else:
        i=i+1

print("Girdiginiz sayilardan pozitif sayilarin toplami: ", toplam)