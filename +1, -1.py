#pc bi 3 haneli sayı tutsun
#bize tahmin şansı sunsun
#önce sayıda herehangi bir sayı doğru yerdeyse +1 yanlış yerdeyse -1 koysun
#doğru bilirsem bildiniz desin

from distutils.command.build_scripts import first_line_re
import random

print("bu oyunda bigisayar 3 basamaklı bir sayı tutar ve sizin tahminlerinize göre eğer sizin tuttuğunuz sayıdaki bsayı da doğru basamağı da doğruysa +1 verir, eğer sayısı doğru basamağı yanlışsa -1 verir, sayıların hepsi yanlış ise 0 verir ")
print("Not: 3 haneli girdiğiniz sayıların rakamları farklı olmalıdır.")

def randomNum():
    #uygun bir sayı olana kadar random üret ve döndür
    
    while True:
        sayı =random.randint(100,999)

        a = set()
        for i in str(sayı):
            a.add(int(i))
        if len(a) ==3:
            return(sayı)



    
def yorum ():
    sayı = randomNum()
    
    while True:
        
        tahmin  = int(input("> "))
    
    
        tahmini=[]
        sayıi =[]
    
        for i in str(tahmin):
            tahmini.append(i)
        for i in str(sayı):
            sayıi.append(i)

    
        if tahmin == sayı:
            print("doğru")
            break
    
        for i in range (3):
            if tahmini[i] == sayıi[i]:
                print("+1")
            
                sayıi[i]= 31
    
        for i in tahmini:
            kullanıldı= False
            if i in sayıi:
                print("-1")
                kullanıldı=True
        if kullanıldı==False:
            print("0")
        
     
    
            
            
print(yorum())






























    



























































