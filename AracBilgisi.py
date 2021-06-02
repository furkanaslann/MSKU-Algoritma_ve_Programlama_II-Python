import AP_II_Final_Project as ana
class Markalar():
    c_kur = ana.kur


    def honda():
        arac_model = input("Araç modelini giriniz: ")
        arac_model.lower()

        if arac_model == "city":
            adet = int(input("Adet: "))
            ana.Honda_City_Adet += adet
            ana.Honda += adet
            ana.depo_arac += adet
            n_fiyat = float(input("Aracın kursuz fiyatı:"))
            kurlu_fiyat = kur * n_fiyat
            print("Kurlu fiyatı: {}".format(kurlu_fiyat))
            y_fiyat = kurlu_fiyat + (kurlu_fiyat * (18 / 100))  # Güncel fiyatı-½18 kar
            lansman_fiyat = kurlu_fiyat + (kurlu_fiyat * (10 / 100))  # lansman fiyatı-%10 kar
            print("Güncel fiyatı: {}".format(y_fiyat))
            print("Lansman fiyatı: {}".format(lansman_fiyat))
            kazanc = lansman_fiyat * 10 / 100
            ana.toplam_kar += kazanc


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
            kazanc = lansman_fiyat * 10 / 100



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
            kazanc = lansman_fiyat * 10 / 100



    def renault(self):
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
            kazanc = lansman_fiyat * 10 / 100


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
            kazanc = lansman_fiyat * 10 / 100



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
            kazanc = lansman_fiyat * 10 / 100



    def peugeot(self):
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
            kazanc = lansman_fiyat * 10 / 100



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
            kazanc = lansman_fiyat * 10 / 100



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
            kazanc = lansman_fiyat * 10 / 100
