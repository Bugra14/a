# Klavyeden girilen 5 sayıdan tek sayı olanları toplayan programı for döngüsü kullanarak kodlayınız. 
# Test edilecek sayılar 4, 7, 11, 14, 9 ve sonuç 27 çıkacaktır

toplam = 0 

for i in range(0,5):
    tekSayi = int(input("Toplanacak sayiyilardan {}.sayiyi girniz: ".format(i+1)))
    if tekSayi%2 != 0:
        toplam = toplam + tekSayi
        i= i+1
    else:
        i=i+1    
    
print("Girdiginiz sayilardan tek sayilarin toplami: ", toplam)   