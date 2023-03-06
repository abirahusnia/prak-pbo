#tugas prak 2 RB
#121140113 Abira Husnia

#class
class Data:
    #konstruktor
    def __init__(self, nama, nim, kelas, sks, semester):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks = sks
        self.semester = semester

    #method
    def data_siakad(self):
        print("Nama             : ", self.nama)
        print("NIM              : ", self.nim)
        print("Kelas Siakad PBO : ", self.kelas)
        print("Jumlah SKS       : ", self.sks)
        print("Semester         : ", self.semester)

#objek        
d1 = Data("Abira Husnia", "121140113", "RB", "22", "4")
d1.data_siakad()
