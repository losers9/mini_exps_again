class Person():
    yil = 2022
    def __init__(self, isim,soyisim, dogumyili, baslamatarihi):
        self.isim = isim
        self.soyisim = soyisim
        self.dogumyili = dogumyili
        self.baslamatarihi = baslamatarihi


class Ogrenci():
    yil = 2022    
    def __init__(self,isim, dogumyili):
        self.dogumyili = dogumyili
        self.isim = isim        
    def yas_bul(self):

        return self.yil - self.dogumyili

class Ogretmen(Person):
    yil = 2022
    def __init__ (self, isim, soyisim, dogumyili, baslamatarihi):
        Person.__init__(self, isim, soyisim, dogumyili, baslamatarihi)
    def sene_hesapla(self):
        return self.yil - self.baslamatarihi  

o1 = Ogrenci('kaan', 1999)
ogretmen1 = Ogretmen('kaan','k',2000, 1990)

print('Yas' , o1.yas_bul())
print('Ogretmen meslek tarihi : ' ,  ogretmen1.sene_hesapla() )
print("inheritance learning almost fin")