import datetime
import random

print("\n***KARDEŞLER OTOMOTİV SATIŞ TEMSİLCİSİ EKRANI*** \n\n")

#YIL-AY-GÜN
#x = datetime.datetime.now()
#print(x.strftime("%c"))

# Her sistem açılışında tablo olarak depoda markaların kaç arabası olduğunu gösterecektir (Deneme için sistem  ilk çalıştığında
#rastgele bir sayı verilecektir.
depo_arac = 0

#Sisteme ilk girişte değişkenleri tanımlamak ve veri karışıklığını önlemek için bu kısımda tek sefer çalıştırmak üzeere değişkenler için rastgele sayı atanıyor.
for a in range(1):
    if depo_arac == 0:
        depo_arac.randint(200, 15000)
        if 10000 < depo_arac < 15000:
            #Bu kısımda markanın modellerine ise aynı şekilde random sayı belirlenecek.
            Renualt = depo_arac - 105
            Honda = (depo_arac - Renualt) - 438
            Peugeot = (depo_arac - Honda - Renault) - 458

        elif 1000 < depo_arac <= 1000:
            #Bu kısımda markanın modellerine ise aynı şekilde random sayı belirlenecek.

            Renualt = depo_arac - 105
            Honda = (depo_arac - Renualt) - 438
            Peugeot = (depo_arac - Honda - Renualt) - 458

def haftalik_hesap():
    sonuc_kar = toplam_kar/hafta_sayisi #Deneme için rastgele sayılar verilecektir başta.
    print("Hafta bazında şirketin kazancı: ", sonuc_kar)

def aylik_hesap():
    sonuc_kar = toplam_kar/ay_sayisi #Deneme için rastgele sayılar verilecektir başta.
    print("Ay bazında şirketin kazancı: ", sonuc_kar)

def dosya_yazma():
    Musteri_Talep_Onay = open("Musteri_talep_onay_dosyasi.txt", "a")
    Musteri_Talep_Onay.write(m_onay_formu_dosya)
    Musteri_Talep_Onay.close()

def karar():
    if secim == "kar hesaplama":
        print("Hesaplamak istediğiniz değer?(haftalık/aylık)")
        deger = input()
        deger.lower()

        if deger == "haftalık":
            if gun < 7:
                print("HATA! Yapmak istediğiniz işlem askıya alınmıştır. Lütfen tekrar deneyiniz!")
                secim()

            elif gun >= 7:
                haftalik_hesap()

        elif deger == "aylık":
            if gun < 30:
                print("HATA! Yapmak istediğiniz işlem askıya alınmıştır. Lütfen tekrar deneyiniz!")
                secim()

            elif gun >= 30:
                aylik_hesap()

    elif secim == "çıkış":
        cikis()

    elif secim == "talep formu":
        musteri_araci()
        kontrol()

        onay = input("Müşteri talebini onaylıyor musunuz? \n")
        onay.lower()

        if onay == "evet":
            dosya_yazma()
            #Aynı zamanda dosyaya bu kısım yazdırılacak.
        elif onay == "hayır":
            print("\nSisteme yönlendiriliyorsunuz...\n")
            secim()
    else:
        cikis()


def secim():
    print('''Yapmak istediğinizi seçiniz: 
-Kar Hesaplama
-Talep Formu
-Çıkış
''')
    breakpoint()
    secim = input()
    secim.lower()
    karar()



def cikis():
    print("Çıkış yapmak istiyor musunuz?")
    cikis = input()
    cikis.lower()

    if cikis == "evet":
        print("İyi günler dileriz.")

    elif cikis == "hayır":
        secim()

def musteri_araci():
    m_ad_soyad = input("Müşterinin adı-soyadı: ")
    m_kimlik = int(input("Kimlik: "))
    m_telefon = int(input("Telefon numarası: "))
    m_email = input("E-mail: ")
    m_adres = input("Adresi:")
    m_arac_marka = input("Araç markası: ")
    m_arac_model = input("Araç modeli: ")
    m_arac_marka.lower()
    m_arac_model.lower()

    m_onay_formu_dosya = '''                KARDEŞLER OTOMOTİV 

Müşterinin;                                         Satıcı;
Adı-Soyadı: {}                                      Adı-Soyadı: {}(Satış Temsilcisi)
T.C. Kimlik: {}                                     Adres: Maslak, 8. Sk. 270-285, 34398 Şişli/İstanbul
Telefon Numarası: {}                                İmza
E-mail: {}
Talep Edilen Araç Markası: {}
Talep Edilen Araç Modeli: {} 
Adres: {}
İmza
    '''.format(m_ad_soyad, danisman, m_kimlik, m_telefon, m_email, m_arac_marka, m_arac_model, m_adres)

    print("Araç bilgileri kontrol ediliyor. Lütfen bekleyiniz!")


def kontrol():
    if m_arac_marka == "honda":
        if m_arac_model == "city":
            if honda_city_adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                honda_city_adet -= 1

            elif honda_city_adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()
                karar()

        elif m_arac_model == "civic":
            if honda_civic_adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                honda_civic_adet -= 1

            elif honda_civic_adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()
                karar()

        elif m_arac_model == "accord":
            if honda_accord_adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                honda_accord_adet -= 1

            elif honda_accord_adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()
                karar()

    if m_arac_marka == "renault":
        if m_arac_model == "megane":
            if renault_megane_adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                renault_megane_adet -= 1

            elif renault_megane_adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()
                karar()

        elif m_arac_model == "clio":
            if renault_clio_adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                renault_clio_adet -= 1

            elif renault_clio_adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()
                karar()

        elif m_arac_model == "kangoo":
            if renault_kangoo_adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                renault_kangoo_adet -= 1

            elif renault_kangoo_adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()
                karar()

    if m_arac_marka == "peugeot":
        if m_arac_model == "208":
            if peugeot_208_adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                peugeot_208_adet -= 1

            elif peugeot_208_adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()
                karar()

        elif m_arac_model == "308":
            if peugeot_308_adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                peugeot_308_adet -= 1

            elif peugeot_308_adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()
                karar()

        elif m_arac_model == "508":
            if peugeot_508_adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                peugeot_508_adet -= 1

            elif peugeot_508_adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()
                karar()


def honda():
    arac_model = input("Araç modelini giriniz: ")
    arac_model.lower()

    if arac_model == "city":
        adet = int(input("Adet: "))
        honda_city_adet += adet
        n_fiyat = float(input("Aracın kursuz fiyatı:"))
        kurlu_fiyat = kur * n_fiyat
        print("Kurlu fiyatı: {}".format(kurlu_fiyat))
        y_fiyat = kurlu_fiyat + (kurlu_fiyat * (18 / 100))  # Güncel fiyatı-½18 kar
        lansman_fiyat = kurlu_fiyat + (kurlu_fiyat * (10 / 100))  # lansman fiyatı-%10 kar
        print("Güncel fiyatı: {}".format(y_fiyat))
        print("Lansman fiyatı: {}".format(lansman_fiyat))


    elif arac_model == "civic":
        adet = int(input("Adet: "))
        honda_civic_adet += adet
        n_fiyat = float(input("Aracın yurt dışı fiyatı:"))
        kurlu_fiyat = kur * n_fiyat
        print("Kurlu fiyatı: {}".format(kurlu_fiyat))
        y_fiyat = kurlu_fiyat + (kurlu_fiyat * (18 / 100))  # Güncel fiyatı-½18 kar
        lansman_fiyat = kurlu_fiyat + (kurlu_fiyat * (10 / 100))  # lansman fiyatı-%10 kar
        print("Güncel fiyatı: {}".format(y_fiyat))
        print("Lansman fiyatı: {}".format(lansman_fiyat))



    elif arac_model == "accord":
        adet = int(input("Adet: "))
        honda_accord_adet += adet
        n_fiyat = float(input("Aracın yurt dışı fiyatı:"))
        kurlu_fiyat = kur * n_fiyat
        print("Kurlu fiyatı: {}".format(kurlu_fiyat))
        y_fiyat = kurlu_fiyat + (kurlu_fiyat * (18 / 100))  # Güncel fiyatı-½18 kar
        lansman_fiyat = kurlu_fiyat + (kurlu_fiyat * (10 / 100))  # lansman fiyatı-%10 kar
        print("Güncel fiyatı: {}".format(y_fiyat))
        print("Lansman fiyatı: {}".format(lansman_fiyat))



def renault():
    arac_model = input("Araç modelini giriniz: ")
    arac_model.lower()

    if arac_model == "megane":
        adet = int(input("Adet: "))
        renault_megane_adet += adet
        n_fiyat = float(input("Aracın yurt dışı fiyatı:"))
        kurlu_fiyat = kur * n_fiyat
        print("Kurlu fiyatı: {}".format(kurlu_fiyat))
        y_fiyat = kurlu_fiyat + (kurlu_fiyat * (18 / 100))  # Güncel fiyatı-½18 kar
        lansman_fiyat = kurlu_fiyat + (kurlu_fiyat * (10 / 100))  # lansman fiyatı-%10 kar
        print("Güncel fiyatı: {}".format(y_fiyat))
        print("Lansman fiyatı: {}".format(lansman_fiyat))


    elif arac_model == "clio":
        adet = int(input("Adet: "))
        renault_clio_adet += adet
        n_fiyat = int(input("Aracın yurt dışı fiyatı:"))
        kurlu_fiyat = kur * n_fiyat
        print("Kurlu fiyatı: {}".format(kurlu_fiyat))
        y_fiyat = kurlu_fiyat + (kurlu_fiyat * (18 / 100))  # Güncel fiyatı-½18 kar
        lansman_fiyat = kurlu_fiyat + (kurlu_fiyat * (10 / 100))  # lansman fiyatı-%10 kar
        print("Güncel fiyatı: {}".format(y_fiyat))
        print("Lansman fiyatı: {}".format(lansman_fiyat))



    elif arac_model == "kangoo":
        adet = int(input("Adet: "))
        renault_kangoo_adet += adet
        n_fiyat = int(input("Aracın yurt dışı fiyatı:"))
        kurlu_fiyat = kur * n_fiyat
        print("Kurlu fiyatı: {}".format(kurlu_fiyat))
        y_fiyat = kurlu_fiyat + (kurlu_fiyat * (18 / 100))  # Güncel fiyatı-½18 kar
        lansman_fiyat = kurlu_fiyat + (kurlu_fiyat * (10 / 100))  # lansman fiyatı-%10 kar
        print("Güncel fiyatı: {}".format(y_fiyat))
        print("Lansman fiyatı: {}".format(lansman_fiyat))



def peugeot():
    arac_model = input("Araç modelini giriniz: ")
    arac_model.lower()

    if arac_model == "200":
        adet = int(input("Adet: "))
        peugeot_208_adet += adet
        n_fiyat = float(input("Aracın yurt dışı fiyatı:"))
        kurlu_fiyat = kur * n_fiyat
        print("Kurlu fiyatı: {}".format(kurlu_fiyat))
        y_fiyat = kurlu_fiyat + (kurlu_fiyat * (18 / 100))  # Güncel fiyatı-½18 kar
        lansman_fiyat = kurlu_fiyat + (kurlu_fiyat * (10 / 100))  # lansman fiyatı-%10 kar
        print("Güncel fiyatı: {}".format(y_fiyat))
        print("Lansman fiyatı: {}".format(lansman_fiyat))



    elif arac_model == "308":
        adet = int(input("Adet: "))
        peugeot_308_adet += adet
        n_fiyat = int(input("Aracın yurt dışı fiyatı:"))
        kurlu_fiyat = kur * n_fiyat
        print("Kurlu fiyatı: {}".format(kurlu_fiyat))
        y_fiyat = kurlu_fiyat + (kurlu_fiyat * (18 / 100))  # Güncel fiyatı-½18 kar
        lansman_fiyat = kurlu_fiyat + (kurlu_fiyat * (10 / 100))  # lansman fiyatı-%10 kar
        print("Güncel fiyatı: {}".format(y_fiyat))
        print("Lansman fiyatı: {}".format(lansman_fiyat))



    elif arac_model == "508":
        adet = int(input("Adet: "))
        peugeot_508_adet += adet
        n_fiyat = int(input("Aracın yurt dışı fiyatı:"))
        kurlu_fiyat = kur * n_fiyat
        print("Kurlu fiyatı: {}".format(kurlu_fiyat))
        y_fiyat = kurlu_fiyat + (kurlu_fiyat * (18 / 100))  # Güncel fiyatı-½18 kar
        lansman_fiyat = kurlu_fiyat + (kurlu_fiyat * (10 / 100))  # lansman fiyatı-%10 kar
        print("Güncel fiyatı: {}".format(y_fiyat))
        print("Lansman fiyatı: {}".format(lansman_fiyat))






danisman = input("Satış temsilcisi Adı-Soyadı: ")
gelen_arac = int(input("Bugün gelen araç sayısı (Geçmek için 00'a basın.): "))
if gelen_arac == 00:
    cikis()

else:
    kur = float(input("Güncel Kur: "))

    for i in range(gelen_arac):
        arac_marka = input("Araç markasını giriniz(Renault-Honda-Peugeot): ")
        arac_marka.lower()


        #Her markanın üçer adet modeli vardır. Honda:1-City 2-Civic 3-Accord | Renault:1-Megane 2-Clio 3-Kangoo | Peuogeot:1-208 2-308 3-508
        if arac_marka == "honda":
             honda()

        elif arac_marka == "renault":
            renault()

        elif arac_marka == "peugeot":
            peugoet()





depo_arac += gelen_arac

while True:
    breakpoint()
    secim()
    breakpoint()
    karar()






