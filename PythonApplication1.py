from cv2.gapi import RGB2Gray
from cv2.typing import Range
import numpy as np
import cv2
import matplotlib





def UzaklikBulSerit(resim):
    "'input = resim bir numpy arrary'"
    "'output = integer type uzaklik'"
    
    uzaklik = 0
    x = len(resim)    #len pythonda uzunluk buluyor normalde c de for loop ile bulurdun burda built-in func var
    for i in range(x):   # i yi uzunluk boyunca iterate et
        if resim[1,i]==1.0: # sadece y de yani column da geziniyoruz cunku yatay ile isimiz var ve böylesi daha performansli  time complexity = O(n) diger turlu O(n kare) olur yavaslar
                            #buradaki örnekte diðer taraflar beyaz czgi siyah bu renk deðiþtirilebilir,
            uzaklik+=1      #uzaklik her siyah olmayan noktada 1 artacak 
        else:
            break
    return uzaklik



re1 = np.ones((10,10))        #sadece test amaçli 10 a 10 luk resim yani array ones dedik arkasi beyaz
cv2.line(re1,(5,0),(5,10),(0,255,0),1)  # x=5,y =0 baþlangic x=5 y=10 bitis noktasi, 0,255,0 siyah rengi temsilen, 1 kalinlik

re2 = np.ones((10,10))
cv2.line(re2,(9,0),(9,10),(0,255,0),1)

#print(UzaklikBulSerit(re2))  yorum satirini kaldirip deneyebilirsiniz ikisinde de uzaklik farkli olacak ayrica kanit amacli print('buraya resim gelecek') yapilabilir her eleman gozukur
#print(UzaklikBulSerit(re1))

    
#print(re1)
#print(re2)

#burada 720 x720 resim uretilir  yine ustte belirtildigi gibi baslangic noktalari 400,0 bitis 400,720    3 kalinliginda
def duzCizgiliResim():
    "'output numpy array yani resim uretilip cizgi cizilmis hali'"
    bosResim = np.ones((720,720))
    cv2.line(bosResim,(400,0),(400,720),(0,255,0),3)
    #cv2.line(bosResim,(720,0),(720,720),(0,255,0),3)
    return bosResim
    

def resimMerkezBul(array):
    return len(array)//2


def edgeleme(resim):
    resimgri = np.copy(resim)
    #resimin yedegi olsun diye copy fonksiyonu resim alir tabii
    griSonuc = cv2.cvtColor(resimgri,cv2.COLOR_RGB2GRAY) # iki input parametresi uygulanacak resim ve dönüstürülecek renk
#.
    resim2 = np.ones((900,900))

    blurSonuc = cv2.GaussianBlur(griSonuc,(5,5),0)        #hepsi ilk input olarak uygulanan resmi aliyor zaten, sonrasinda esik deðerleri
    edgeSonuc = cv2.Canny(blurSonuc,50,150)
    return edgeSonuc


#print(len((5,4)))

resim = cv2.imread("abc.jpg")
edgeleme(resim)


print(UzaklikBulSerit(duzCizgiliResim())) 
cv2.imshow("edgeli",edgeleme(resim))
cv2.imshow("resim2",duzCizgiliResim())

#cv2.imshow("iki",resim2)

cv2.waitKey(0)

