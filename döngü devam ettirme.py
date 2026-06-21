defkullanıcı ="yazılımcıbebe"
defparola ="1234"

while(True):
    kullanıcı=input("kullanıcı adı:")
    parola=input("parola:")
    if((defkullanıcı== kullanıcı) and ( defparola==parola)):
        print ("hoşgeldiniz",kullanıcı)
        break
    elif((kullanıcı != defparola) and (defparola== parola)):
        print ("kullanıcı adınız yanlış")
    elif((kullanıcı == defkullanıcı) and (defparola !=parola)):
        print ("Şifrenizi mi unuttunz")
        print ("şifrenizi değiştirmek istermisiniz? (E/H)")
        cevap = input()
        if(cevap =="E"):
            print("Yeni Parola:")
            yeniparola = input ("Yeni Parola:")
            print ("Lütfen Bekleyin")
            defparola = yeniparola
            print("Şifre Başarıyla Değiştirildi")

    else:
        print("TEKRAR DENEYİNİZ")