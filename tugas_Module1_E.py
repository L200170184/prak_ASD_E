print ("Nama : Mochammad Itmamul Wafa"+"\n"+"Nim : L200170184"+"\n"+"Kelas : E")
print("\n")
print("1.")
string = ""
bar = 1

x = int(input("Masukkan angka : "))
while bar <= x:
    kol = bar

    while kol > 0:
        string = string + "*"
        kol = kol - 1

    string = string + '\n'
    bar = bar + 1
print(string)
print("\n")

print("2.")
def PesegiEmpat(a,b):
    i=1
    print("@"*b)
    while(i<a):
       print("@"+" "*(b-2)+"@")
       i+=1
    print("@"*b)
PesegiEmpat(4,5)
print("\n")

print("3.")
def jumlahhurufvokal(a):
    v="aiueoAIUEO"
    vokal=0
    jumlahhuruf=0
    for i in a:
        jumlahhuruf+=1
        if i in v:
            vokal+=1
    return (vokal,jumlahhuruf)
print(jumlahhurufvokal("surakarta"))
def jumlahhurufkonsonan(a):
    v="bcdfghjklmnpqrstvwxyz"
    konsonan=0
    jumlahhuruf=0
    for i in a:
        jumlahhuruf+=1
        if i in v:
            konsonan+=1
    return (konsonan,jumlahhuruf)
print(jumlahhurufkonsonan("surakarta"))
print("\n")

print("4.")
def rata(b=[]):
    x=0
    n=0
    if b != []:
        for i in b:
            x+=i
            n+=1
        return x/n
    return "illegal"
print(rata([2,2]))
print("\n")

print("5.")
from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primakecil=[2, 3, 5, 7, 11]
    bukanprima=[0, 1, 4, 6, 8, 9, 10]
    if n in primakecil:
        return True
    elif n in bukanprima:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
    return True
print(apakahPrima(71))
print("\n")

print("6.")
def bilanganprima():
    prima=list()
    for i in range(2,100):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if(a):
            print(i)
            prima.append(i)
bilanganprima()
print("\n")

print("7.")
def faktorprima(n):
    prima=list()
    for i in range(2,n):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if a and n%i==0:
            prima.append(i)
    return prima
print(faktorprima(15))
print("\n")

print("8.")
def apakahTerkandung(a,b):
     return a in b
print(apakahTerkandung("db","abcdcdsqwedb"))
print(apakahTerkandung("abd","abc"))
print("\n")

print("9.")
def iterasi():
    for i in range(1,100):
        if (i%3)!=0 and (i%5)!=0:
            print(i)
        else:
            if (i%15)==0:
                print("pyton UMS")
            elif (i%3)==0:
                print("python")
            elif (i%5)==0:
                print("UMS")
iterasi()
print("\n")

print("10.")
def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2)-(4*a*c)
    if D<0:
        return "determinan negatif"
    return  "determinan positif"
print(selesaikanABC(1,1,2))
print("\n")

print("11.")
def apakahKabisat(a):
    if(a%400==0):
        return True
    if(a%100==0):
        return False
    if(a%4==0):
        return True
    return False
print(apakahKabisat(100))
print("\n")

print("12.")
import random
def permainan():
    a=random.randrange(0, 100)
    while(True):
        b=int(input("masukan angka: "))
        if(b>a):
            print("terlalu besar, coba lagi")
        elif(b<a):
            print("terlalu kecil, coba lagi")
        else:
            print("benar")
            break
permainan()
print("\n")

print("13.")
def katakan(a):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",-6:"ratus ",-7:"juta ",-8:"puluhjuta ",-9:"ratusanjutta "}
    b=str(a)
    c=""
    i=-1
    while i>= -len(b):
        c=x[b[i]]+y[i]+c
        i-=1
    return c
print(katakan(555))
print("\n")

print("14")
def formatRupiah(a):
    b=str(a)
    c=""
    i = -1
    while i>= -len(b):
        if((i+1)%3==0 and (i+1)!=0):
            c="."+c
        c=b[i]+c
        i-=1
    return "Rp "+c
print(formatRupiah(25000000))
