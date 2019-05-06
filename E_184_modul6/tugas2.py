class manusia(object):
    """ clas manusia dengan inisiasi 'nama' """
    keadaan='lapar'
    def __init__(self,nama):
        self.nama=nama
    def ucap(self):
        print("halo namaku: ",self.nama)
    def olah(self,k):
        print('saya habis',k)
        self.keadaan='lapar'
    def makan(self,s):
        print("saya baru saja makan ",s)
        self.keadaan='kenyang'
    def kali(self,n):
        return n*2

class mahasiswa(manusia):
    """ class mahsiswa yang dibangun dai class manusia """
    def __init__(self,nama,NIM,kota,us):
        self.Nama=nama
        self.NIM=NIM
        self.kota=kota
        self.us=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilin(self):
        return self.Nama
    def ambilnim(self):
        return self.NIM
    def ambiluang(self):
        return self.uang
    def makan(self,s):
        print ("saya makan",s)
        self.keadaan='kenyang'
    def pkota(self):
        return self.kota
    def perbarui(self,x):
        self.kota=x
    def tambah(self,x):
        self.uang=self.uang+x
