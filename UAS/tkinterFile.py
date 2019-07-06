from tkinter import filedialog
from tkinter import *
import subprocess
import os, os.path
import time


root = Tk()
root.withdraw()
z = []
    
def ambil():
    root = Tk()
    root.withdraw()
    z = []
    filez = filedialog.askopenfilenames(parent=root,title='Choose a file')
    a = root.tk.splitlist(filez)
    aww = []
    zzz = ""
    for i in range(len(a)):
        z.append(a[i])
        aww.append(os.path.basename(a[i]))

    
    awz = os.path.dirname(a[0])
    print(awz)
    print(os.stat(a[0]).st_size)
    for i in range(len(aww)):
        zzz = zzz + aww[i] + "\n"


##    for i in range(len(z)):
##        print(z[i])
##        subprocess.Popen(['C:/Program Files (x86)/VideoLAN/VLC/vlc.exe', "\\"+z[i]])
##        time.sleep(0.01)    
##


