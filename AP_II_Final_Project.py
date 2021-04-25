import datetime

#YIL-AY-GÜN
x = datetime.datetime.now()
print(x.strftime("%c"))

danisman = input("Satış Temsilcisi Adı-Soyadı: ")
gelen_arac = int(input("Bugün gelen araç sayısı: "))
gelen_arac_ozellik = input("Özellikleri: ")
toplam_depo = input("Depodaki Toplam araç sayısı: ")

print("\nSisteme yönlendiriliyorsunuz...\n")

while True:
    print('''Yapmak istediğinizi seçiniz: 
-Kar Hesaplama
-Talep Formu
-Çıkış
''') #fonksiyon çağrılacak.
    secim = input()
    secim.lower()

    if secim == "kar hesaplama":
        print("Hesaplamak istediğiniz değer?(haftalık/aylık)")
        deger = input()
        deger.lower()

        if deger == "haftalık":
            if gun < 7:
                print("HATA! Yapmak istediğiniz işlem askıya alınmıştır. Lütfen tekrar deneyiniz!")
                break

            elif gun >= 7:
                #Fonksiyon çağrılıp hesaplama yapılacak.

        elif deger == "aylık":
            if gun < 30:
                print("HATA! Yapmak istediğiniz işlem askıya alınmıştır. Lütfen tekrar deneyiniz!")

            elif gun >= 30:
                #Fonksiyon çağrılıp hesaplama yapılacak.
    elif secim == "çıkış":
        #Çıkış fonksiyonu.

    else secim == "talep formu":
        m_ad_soyad = input("Müşterinin adı-soyadı: ")
        m_kimlik = int(input("Kimlik: "))
        m_telefon = int(input("Telefon numarası: "))
        m_email = input("E-mail: ")
        m_arac = input("Talep edilen araç (Marka-Model-Paket): ")

        #Talep edilen araç bilgileri kontrol edilecek.

        onay = input("Müşteri talebini onaylıyor musunuz? \n")
        onay.lower()

        if onay == "evet":
            #Onay formu fonksiyonuna gidecek.
            #Aynı zamanda dosyaya bu kısım yazdırılacak.
    #Çıkış fonksiyonuna gidilecek.



