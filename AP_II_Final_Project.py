import datetime
import random
import AracBilgisi as sinif
import Musteri as musteri

print("\n***KARDEŞLER OTOMOTİV SATIŞ TEMSİLCİSİ EKRANI*** \n\n")

#Depodaki araç sayısını tanımlamak için ilk başta bu kısmı tek seferliğine yazdırıyorum.
for i in range(1):

    depo_arac = 15874
    Renault = 5126
    Renault_Clio_Adet = 3781
    Renault_Megane_Adet = 1065
    Renault_Kangoo_Adet = 280

    Honda = 4168
    Honda_City_Adet = 254
    Honda_Civic_Adet = 3045
    Honda_Accord_Adet = 869

    Peugeot = 6580
    Peugeot_208_Adet = 3336
    Peugeot_308_Adet = 1086
    Peugeot_508_Adet = 2158


def cikis():
    durum = input("Sistemden çıkış yapmak istiyor musunuz?: ")
    durum.lower()
    if durum == "evet":
        return False

    elif durum == "hayır":
        return True

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


def secim():
    print('''Yapmak istediğinizi seçiniz: 
-Kar Hesaplama
-Talep Formu
-Çıkış
''')

    bildirme = input()
    bildirme.lower()
    return bildirme


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

    x = datetime.datetime.now()
    tarih = x.strftime("%c")

    m_onay_formu_dosya = '''                KARDEŞLER OTOMOTİV 

Müşterinin;                                         Satıcı;
Adı-Soyadı: {}                                      Adı-Soyadı: {}(Satış Temsilcisi)
T.C. Kimlik: {}                                     Adres: Maslak, 8. Sk. 270-285, 34398 Şişli/İstanbul
Telefon Numarası: {}                                İmza
E-mail: {}
Talep Edilen Araç Markası: {}
Talep Edilen Araç Modeli: {} 
Adres: {}
İmza                                                Tarih: {}
    '''.format(m_ad_soyad, danisman, m_kimlik, m_telefon, m_email, m_arac_marka, m_arac_model, m_adres, tarih)

    x = datetime.datetime.now()
    print(x.strftime("%c"))
    print("Araç bilgileri kontrol ediliyor. Lütfen bekleyiniz!")

    return m_onay_formu_dosya, m_ad_soyad, m_kimlik, m_telefon, m_email, m_adres, m_arac_marka, m_arac_model, tarih


def kontrol():
    if m_arac_marka == "honda":
        if m_arac_model == "city":
            if Honda_City_Adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                Honda_City_Adet -= 1
                Honda -= 1
                depo_arac -= 1

            elif Honda_City_Adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()

        elif m_arac_model == "civic":
            if Honda_Civic_Adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                Honda_Civic_Adet -= 1
                Honda -= 1
                depo_arac -= 1

            elif Honda_Civic_Adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()

        elif m_arac_model == "accord":
            if Honda_Accord_Adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                Honda_Accord_Adet -= 1
                Honda -= 1
                depo_arac -= 1

            elif Honda_Accord_Adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()

    if m_arac_marka == "renault":
        if m_arac_model == "megane":
            if Renault_Megane_Adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                Renault_Megane_Adet -= 1
                Renault -= 1
                depo_arac -= 1

            elif Renault_Megane_Adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()

        elif m_arac_model == "clio":
            if Renault_Clio_Adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                Renault_Clio_Adet -= 1
                Renault -= 1
                depo_arac -= 1

            elif Renault_Clio_Adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()

        elif m_arac_model == "kangoo":
            if Renault_Kangoo_Adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                Renault_Kangoo_Adet -= 1
                Renault -= 1
                depo_arac -= 1

            elif Renault_Kangoo_Adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()

    if m_arac_marka == "peugeot":
        if m_arac_model == "208":
            if Peugeot_208_Adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                Peugeot_208_Adet -= 1
                Peugeot -= 1
                depo_arac -= 1

            elif Peugeot_208_Adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()

        elif m_arac_model == "308":
            if peugeot_308_adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                peugeot_308_adet -= 1

                depo_arac -= 1

            elif peugeot_308_adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()
                karar()

        elif m_arac_model == "508":
            if peugeot_508_adet >= 1:
                print("Aradığınız model araç bulunmuştur. Lütfen bekleyiniz!")
                peugeot_508_adet -= 1
                depo_arac -= 1

            elif peugeot_508_adet < 1:
                print("Aradığınız model araç bulunmamaktadır!\n Sisteme yönlendiriliyorsunuz...\n")
                secim()


def karar(bildirme):
    if bildirme == "kar hesaplama":
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

    elif bildirme == "çıkış":
        cikis()

    elif bildirme == "talep formu":
        musteri_araci()
        kontrol()

        onay = input("Müşteri talebini onaylıyor musunuz? \n")
        onay.lower()

        if onay == "evet":
            dosya_yazma()

        elif onay == "hayır":
            print("\nSisteme yönlendiriliyorsunuz...\n")
            secim()

#Sisteme ilk girişte değişkenleri tanımlamak ve veri karışıklığını önlemek için bu kısımda tek sefer çalıştırmak üzeere değişkenler için rastgele sayı atanıyor.
for a in range(1):
    if depo_arac == 0:
        depo_arac = random.randint(200, 15000)
        if 10000 < depo_arac < 15000:
            #Bu kısımda markanın modellerine aynı şekilde random sayı belirlenecek.
            Renault = depo_arac - 105


            Honda = (depo_arac - Renault) - 438
            Peugeot = (depo_arac - Honda - Renault) - 458

        elif 1000 < depo_arac <= 1000:
            #Bu kısımda markanın modellerine aynı şekilde random sayı belirlenecek.

            Renault = depo_arac - 105
            Honda = (depo_arac - Renault) - 438
            Peugeot = (depo_arac - Honda - Renault) - 458




danisman = input("Satış temsilcisi Adı-Soyadı: ")
gelen_arac = int(input("Bugün gelen araç sayısı (Geçmek için 00'a basın.): "))

if gelen_arac == 00:
    print("Sisteme yönlendiriliyorsunuz...")
    False

else:
    kur = float(input("Güncel Kur: "))


    for i in range(gelen_arac):
        arac_marka = input("Araç markasını giriniz(Renault-Honda-Peugeot): ")
        arac_marka.lower()

        if arac_marka == "honda":
            sinif.Markalar.honda()

        elif arac_marka == "renault":
            sinif.Markalar.renault()

        elif arac_marka == "peugeot":
            sinif.Markalar.peugeot()





depo_arac += gelen_arac

while True:
    secim()
    karar(bildirme)






