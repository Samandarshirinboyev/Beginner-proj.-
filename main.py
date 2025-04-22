import datetime

def ortalama_hesapla():
    sayilar = input("Sayıları aralarında boşluk olacak şekilde girin: ").split()
    sayilar = [float(sayi) for sayi in sayilar]
    ort = sum(sayilar) / len(sayilar)
    print(f"Ortalama: {ort:.2f}")

def hesap_makinesi():
    print("İşlemler: +, -, *, /")
    sayi1 = float(input("1. sayı: "))
    islem = input("İşlem: ")
    sayi2 = float(input("2. sayı: "))

    if islem == "+":
        print("Sonuç:", sayi1 + sayi2)
    elif islem == "-":
        print("Sonuç:", sayi1 - sayi2)
    elif islem == "*":
        print("Sonuç:", sayi1 * sayi2)
    elif islem == "/":
        if sayi2 != 0:
            print("Sonuç:", sayi1 / sayi2)
        else:
            print("Sıfıra bölünemez!")
    else:
        print("Geçersiz işlem.")

def yas_bul():
    dogum_yili = int(input("Doğum yılınızı girin: "))
    suanki_yil = datetime.datetime.now().year
    yas = suanki_yil - dogum_yili
    print(f"Yaşınız: {yas}")

def bmi_hesapla():
    kilo = float(input("Kilonuzu girin (kg): "))
    boy = float(input("Boyunuzu girin (metre): "))
    bmi = kilo / (boy ** 2)
    print(f"BMI: {bmi:.2f}")
    if bmi < 18.5:
        print("Zayıf")
    elif bmi < 24.9:
        print("Normal")
    elif bmi < 29.9:
        print("Fazla kilolu")
    else:
        print("Obez")

def not_ortalamasi():
    ders_sayisi = int(input("Kaç dersiniz var?: "))
    toplam = 0
    for i in range(ders_sayisi):
        notu = float(input(f"{i+1}. dersin notunu girin: "))
        toplam += notu
    ort = toplam / ders_sayisi
    print(f"Not Ortalaması: {ort:.2f}")

def menu():
    while True:
        print("\n--- Matematiksel Araç Kutusu ---")
        print("1. Ortalama Hesapla")
        print("2. Hesap Makinesi")
        print("3. Yaş Hesapla")
        print("4. Vücut Kitle İndeksi Hesapla")
        print("5. Not Ortalaması Hesapla")
        print("0. Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            ortalama_hesapla()
        elif secim == "2":
            hesap_makinesi()
        elif secim == "3":
            yas_bul()
        elif secim == "4":
            bmi_hesapla()
        elif secim == "5":
            not_ortalamasi()
        elif secim == "0":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.")

menu()