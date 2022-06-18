import random
liste=[]
basla=input("Oyunu başlatmak için 'başlat', iptal etmek için 'iptal' yazınız.")
while True:
    try:
        giris=input("Çekilişe katılacak kişiler:")
        if giris=="iptal":
            sor=input("Kişi mi iptal etmek istiyorsun (kisi), cekilis mi iptal etmek istiyorsun (cekilis)")
            if sor=="kisi":
                sor1=input("Kimi iptal etmek istiyorsunuz? \n")
                if sor1 in liste:
                    yer=liste.index(sor1)
                    liste.pop(yer)
                    print("Bu kişiyi çekilişten iptal ettik.")
                    print(liste)
                else:
                     print("Böyle bir kişi çekilişte yoktur.")
                     print(liste)
            elif sor=="cekilis":
                try:
                    while True:
                        liste.pop()
                except:
                    print("Çekiliş iptal edilmiştir.")

        elif giris=="başlat":
            sor2=int(input("Kazanacak kişi sayısı girin:"))
            sonuc=random.sample(liste,sor2) 
            if len(liste)<sor2:
                print("Kazanacak kişi sayısı liste sayısından büyük olamaz. \n Lütfen tekrar deneyin.")
            else:
                print("Kazananlar:",sonuc)
        else:
            liste.append(giris)

    except:
        print("Hatalı giriş yaptınız. Lünfen tekrar deneyin.")
  