# Klavyeden girilen 5 sayıdan çift sayı olanları toplayan programı for döngüsü kullanarak kodlayınız. 
# Test edilecek sayılar 6, 15, 22, 4, 13 ve sonuç 32 çıkacaktır

toplam= 0 

for i in range(0,5):
    ciftSayi = int(input("Toplanacak sayilardan {}. sayiyi girniz: ".format(i+1)))
    if ciftSayi%2 ==0 :
        toplam = toplam+ciftSayi
        i= i+1
    else:
        i= i+1    

print("Girdiginiz sayilardan cift sayilarin toplami: ",toplam)        