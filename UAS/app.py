from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tkinter import filedialog
from tkinter import *
from iniqueue import *
import subprocess
import os
import time
import sys
from gui import *
from tkinterFile import *
import pygame
root = Tk()
root.withdraw()
class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.namafolder = ""
        self.isifolder = []
        self.file = []
        self.daftar = []
        self.e = ""

        self.tandaCari = 0
        self.indexCari = 0
        self.listCari = []
    
        self.index = 0
        self.pushButton.clicked.connect(self.tambah)
        self.pushButton_4.clicked.connect(self.cari)
        self.pushButton_3.clicked.connect(self.urutkan)
        self.pushButton_6.clicked.connect(self.hapus)
        self.pushButton_7.clicked.connect(self.putar)
        self.pushButton_2.clicked.connect(self.selanjutnya)
        self.pushButton_5.clicked.connect(self.sebelumnya)
        
    def tambah(self):
        self.e = ""
        self.namafolder = filedialog.askopenfilenames(parent=root, title='pilih file')
        self.isifolder = root.tk.splitlist(self.namafolder)
        
        for i in range(len(self.isifolder)):
            self.file.append(self.isifolder[i])
            self.daftar.append(os.path.basename(self.isifolder[i]))
        for i in range(len(self.daftar)):
            self.e = self.e + self.daftar[i] + "\n"
        self.textEdit.setText(self.e)

    def buatTabel(self):
        self.filesTable = QtGui.QTableWidget(0, 7)
        self.filesTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

        self.filesTable.setHorizontalHeaderLabels(("No.", "Nama", "Tipe", "Ukuran", "Akses", "Dibuat", "Lokasi"))
        self.filesTable.horizontalHeader().setResizeMode(6, QtGui.QHeaderView.Stretch)
        self.filesTable.verticalHeader().hide()
        self.filesTable.setShowGrid(False)

        self.filesTable.setColumnWidth(0, 40)
        self.filesTable.setColumnWidth(2, 50)
        self.filesTable.setColumnWidth(3, 60)
        self.filesTable.setColumnWidth(4, 80)
        self.filesTable.setColumnWidth(5, 80)

        self.connect(self.filesTable, QtCore.SIGNAL('cellDoubleClicked(int, int)'),self.bukaFIle)
        
    def urutkan(self):
        self.tandaCari = 0
        self.e = ""
        self.daftar = []
        
        n = len(self.file)

        for i in range(n):
            for j in range(0, n-i-1):
                if self.file[j] > self.file[j+1] :
                    self.file[j], self.file[j+1] = self.file[j+1], self.file[j]
                    
        for i in range(len(self.file)):
            self.daftar.append(os.path.basename(self.file[i]))

        for i in range(len(self.daftar)):
            self.e = self.e + self.daftar[i] + "\n"
        self.textEdit.setText(self.e)

    
    def cari(self):
        self.tandaCari = 1
        self.e = ""
        self.daftar = []
        self.listCari = []
        target = self.lineEdit.text()
        for i in range(len(self.file)):
            if target.lower() in self.file[i].lower():
                self.listCari.append(self.file[i])
                
        for i in range(len(self.listCari)):
            self.daftar.append(os.path.basename(self.listCari[i]))

        for i in range(len(self.daftar)):
            self.e = self.e + self.daftar[i] + "\n"
        self.textEdit.setText(self.e)
                
    def hapus(self):
        self.e = ""
        self.daftar = []
        self.file.pop(len(self.file)-1)
        for i in range(len(self.file)):
            self.daftar.append(os.path.basename(self.file[i]))

        for i in range(len(self.daftar)):
            self.e = self.e + self.daftar[i] + "\n"
        self.textEdit.setText(self.e)

    def putar(self):
        if self.tandaCari == 0:
            self.index = 0
            pygame.init()
            pygame.mixer.music.load(self.file[self.index])
            pygame.mixer.music.play()
        else:
            self.indexCari = 0
            pygame.init()
            pygame.mixer.music.load(self.listCari[self.indexCari])
            pygame.mixer.music.play()

    def selanjutnya(self):
        try:
            if self.tandaCari == 0:

                self.index += 1
                pygame.init()
                pygame.mixer.music.load(self.file[self.index])
                pygame.mixer.music.play()
            else:
                self.indexCari += 1
                pygame.init()
                pygame.mixer.music.load(self.listCari[self.indexCari])
                pygame.mixer.music.play()
        except:
            self.index = -1
            self.indexCari = -1
            if self.tandaCari == 0:
                self.index += 1
                pygame.init()
                pygame.mixer.music.load(self.file[self.index])
                pygame.mixer.music.play()
            else:
                self.indexCari += 1
                pygame.init()
                pygame.mixer.music.load(self.listCari[self.indexCari])
                pygame.mixer.music.play()
            

    def sebelumnya(self):
        try:
            if self.tandaCari == 0:

                self.index -= 1
                pygame.init()
                pygame.mixer.music.load(self.file[self.index])
                pygame.mixer.music.play()
            else:
                self.indexCari -= 1
                pygame.init()
                pygame.mixer.music.load(self.listCari[self.indexCari])
                pygame.mixer.music.play()
        except:
            self.index = len(self.file)
            self.indexCari = len(self.listCari)
            if self.tandaCari == 0:
                self.index += 1
                pygame.init()
                pygame.mixer.music.load(self.file[self.index])
                pygame.mixer.music.play()
            else:
                self.indexCari += 1
                pygame.init()
                pygame.mixer.music.load(self.listCari[self.indexCari])
                pygame.mixer.music.play()
if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainWindow()
    form.setWindowTitle("Mamulify")
    form.show()
    sys.exit(a.exec_())
    a.exec_()

