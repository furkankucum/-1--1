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

def out(plus,minus):
    o = ""
    if plus >0:
        o+=f"+{plus} "
    if minus >0:
        o+=f"-{minus}"
    if o!="":print(o)
def listele(var):
    o = []
    for i in str(var):
        o.append(i)
    return o
    
def main ():
    sayı = randomNum()
    
    while True:
        kullanıldı= False
        tahmin  = int(input("> "))
        tahmini=listele(tahmin)
        sayıi =listele(sayı)
    
        if tahmin == sayı:
            print("doğru")
            break
        o = ""
        plus = 0
        minus = 0
        for i in range (3):
            if tahmini[i] == sayıi[i]:
                plus+=1
                kullanıldı=True
                sayıi[i]= 31
    
        for i in tahmini:
            if i in sayıi:
                minus+=1
                kullanıldı=True
        out(plus,minus)
        if not kullanıldı:
            print("0")
        
     
    
            
            

























































































main()






























    

























































