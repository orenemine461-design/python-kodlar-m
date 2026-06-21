from operator import truediv

faktoriyel =1

while True:
    sayı= int(input("lütfen negatif olmayan sayı giriniz:"))
    if(sayı<=0):
        print("lütfen negatif olmayan bir sayı giriniz.")
    else:
        for i in range(1,sayı+1):
            faktoriyel *=i

        print("faktoriyel",faktoriyel)
        break
