# Klavyeden girilen 5 sayıdan negatif olanları toplayan programı for döngüsü kullanarak kodlayınız. 
# Test edilecek sayılar -8, 9, 10, -5, -1 ve sonuç -14 çıkacaktır.

toplam=0

for i in range(0,5):
    negatifSayi= int(input("Toplanacak sayilardan {}. sayiyi giriniz: ".format(i+1)))
    
    if negatifSayi<0:
        toplam= toplam + negatifSayi
        i=i+1
    else:
        i=i+1

print("Girdiginiz sayilardan negatif sayilarin toplami: ", toplam)