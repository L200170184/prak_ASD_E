print("No.1")
from datetime import date


class Pesan(object):
    def __init__(self, kata):
        self.kata = kata
    def cetak(self):
        print(self.kata)
    def cetakHurufKapital():
        print(str.upper(self.kata))
    def cetakHurufKecil():
        print(str.lower(self.kata))
    def jumKar(self):
        return len(self.kata)
    def CetakKarakter(self):
        print('kalimat memepunyai',len(sel.kata),'karakter')
    def perbarui(self, stringBaru):
        self.kata=stringBaru
    #a
    def apakahTerkandung(self, yo):
        if yo in self.kata:
            return True
        else:
            return False
    #b
    def hitungKonsonan(self):
        vokal = 'AIUEOaiueo'
        v = 0
        for x in self.kata:
            if x in vokal:
                v+=1
        kon = len(self.kata) - v
        return kon
    #c 
    def hitungVokal(self):
        vokal = 'AIUEOaiueo'
        v = 0
        for x in self.kata:
            if x in vokal:
                v+=1
        return v

