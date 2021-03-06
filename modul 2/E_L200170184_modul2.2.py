print ("No 2")
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


class Mahasiswa(Manusia):
    """Class yang dibangun dari class Manusia"""

    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nim = NIM
        self.kota = kota
        self.us = us
    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    
    def ambilUangSaku(self):
        return self.us

    #c
    def tambahUangSaku(self, tambahUang):
        self.us = self.us + tambahUang
        
    #a
    def ambilKotaTinggal(self):
        return self.kota
    
    #b
    def perbaruiKotaTinggal(self, kotabaru):
        self.kota = kotabaru
        
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau sambil belajar ."""
        print("Saya baru saja makan",s,"sambil belajar")
        self.keadaan = 'kenyang'

m1 = Mahasiswa('Jamil', 134, 'Surakarta', 250000)
m2 = Mahasiswa('Andi', 265, 'Magelang', 275000)
m3 = Mahasiswa('Sri', 376, 'Yogyakarta', 240000)
m4 = Mahasiswa('Jamilah', 144, 'Salatiga', 210000)
m5 = Mahasiswa('Sandi', 275, 'Malang', 215000)
m6 = Mahasiswa('Sriyati', 386, 'Jakarta', 200000)
m7 = Mahasiswa('Sugeng', 135, 'Bali', 280000)
m8 = Mahasiswa('Deni', 276, 'Tasikmalaya', 277000)
m9 = Mahasiswa('Susi', 387, 'Bekasi', 244000)
