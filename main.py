# BKİ Hesaplayıcı
isim = input("Adınız: ")
boy = float(input("Boyunuz (cm): "))
kilo = float(input("Kilonuz (kg): "))

if boy <= 0 or kilo <= 0:
    print("Hata: Boy ve kilo sıfırdan büyük olmalı!")
else:
    boy_metre = boy / 100
    bki = kilo / (boy_metre * boy_metre)
    print(f"{isim}, BKİ değeriniz: {bki:.2f}")

    if bki < 18.5:
        kategori = "Zayıf"
    elif bki < 25:
        kategori = "Normal kilolu"
    elif bki < 30:
        kategori = "Fazla kilolu"
    elif bki < 35:
        kategori = "Obez (1. derece)"
    elif bki < 40:
        kategori = "Obez (2. derece)"
    else:
        kategori = "Obez (3. derece)"

    print(f"Kategoriniz: {kategori}")