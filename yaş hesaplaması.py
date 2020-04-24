import datetime

tarih = datetime.datetime.now()
mevcut_yil = tarih.year
mevcut_yil = int(mevcut_yil)

dogum_yili = int(input("Doğduğunuz yılı giriniz: "))

yas = mevcut_yil - dogum_yili
print("Şu anki yaşınız: ",  yas)
