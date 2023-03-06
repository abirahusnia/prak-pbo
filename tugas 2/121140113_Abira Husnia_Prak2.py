#tugas prak 1 RB
#121140113 Abira Husnia

class Data:
    def __init__(self, nama, nim, kelas, sks, semester):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks = sks
        self.semester = semester
        
d1 = Data("Abira Husnia", "121140113", "RB", "22", "4")
        
print("Nama             : ", d1.nama)
print("NIM              : ", d1.nim)
print("Kelas Siakad PBO : ", d1.kelas)
print("Jumlah SKS       : ", d1.sks)
print("Semester         : ", d1.semester)
