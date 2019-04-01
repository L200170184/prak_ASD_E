class Manusia(object):
    """Class manusia dengan inisiasi 'nama'"""
    keadaan='lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapSalam(self):
        print("halo namaku: ", self.nama)
    def makan(self,s):
        print("saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olah(self,k):
        print('saya baru saja latihan', k)
        self.keadaan='lapar'
    def kali(self,n):
        return n*2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dai class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.NIM=NIM
        self.kota=kota
        self.uang=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUang(self):
        return self.uang
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan='kenyang'
    def ambilKota(self):
        return self.kota
    def perbaruiKota(self,k):
        self.kota=k
    def tambahUang(self,n):
        self.uang+=n

print('1.')
import sys
ms1=Mahasiswa('aa',420,'Solo',420000)
ms2=Mahasiswa('bb',318,'Solo',420000)
ms3=Mahasiswa('cc',732,'Solo',420000)
ms4=Mahasiswa('dd',910,'Solo',420000)
ms5=Mahasiswa('ee',120,'Solo',420000)
ms6=Mahasiswa('ff',190,'Solo',420000)
ms7=Mahasiswa('gg',107,'Solo',420000)
ms8=Mahasiswa('hh',820,'Solo',420000)
ms9=Mahasiswa('ii',290,'Solo',420000)
ms10=Mahasiswa('jj',624,'Solo',420000)


mhss = [ms1,ms2,ms3,ms4,ms5,ms6,ms7,ms8,ms9,ms10]

def urutkan(A):
    baru = {}
    for i in range(len(A)):
        baru[A[i].nama] = A[i].NIM
    listofTuples = sorted(baru.items(), key=lambda x: x[1])
    for elem in listofTuples :
        print(elem[0] , ":" , elem[1] )


urutkan(mhss)

print('\n2')
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def gabung(a,b):
    c = []
    c = a+b
    n = len(c)
    for i in range(n):
        for j in range(0, n-i-1):
            if c[j] > c[j+1] :
                c[j], c[j+1] = c[j+1], c[j]
    return c
a = [9,2,5,11,4,7,19,1]
b = [13,43,56,12,56]
a, b = bubblesort(a), bubblesort(b)

print(a,"\n", b)
print()
print(gabung(a,b))

print('\n3')
from time import time as detak
from random import shuffle as kocok
k = [i for i in range(1,6001)]
kocok(k)

def bubb(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def sele(A):
    for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
        A[i], A[min_idx] = A[min_idx], A[i]

def inse(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

bub = k[:]
sel = k[:]
ins = k[:]

aw=detak();bubb(bub);ak=detak();print('bubble : %g detik' %(ak-aw));
aw=detak();sele(sel);ak=detak();print('selection : %g detik' %(ak-aw));
aw=detak();inse(ins);ak=detak();print('insertion : %g detik' %(ak-aw));

