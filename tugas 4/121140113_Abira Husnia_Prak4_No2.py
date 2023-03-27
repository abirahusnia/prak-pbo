#tugas prak 4 RB
#121140113 Abira Husnia

import random

class Robot:
    jumlah_turn = 0
    alive = True
  
    def __init__(self,nama,health,damage):
        self.nama = nama
        self.health = health
        self.damage = damage
        
    def lakukan_aksi(self,other):
        if self.nama == "Antares":
            if Robot.jumlah_turn%3==0:
                self.damage = self.damage*1.5
                Robot.terima_aksi(other,self.damage)
                self.damage = 5000
                return f""
            else:
                Robot.terima_aksi(other,self.damage)
                return f""

        elif self.nama == "Alphasetia":
            if Robot.jumlah_turn%2==0:
                self.health += 4000
                Robot.terima_aksi(other,self.damage)
                return f"Alphasetia menambah darah sebanyak 4000 HP\n"
            else:
                Robot.terima_aksi(other,self.damage)
                return f"Alphasetia menambah darah sebanyak 4000 HP\n"

        elif self.nama == "Lecalicus":
            if Robot.jumlah_turn%4==0:
                self.damage = self.damage*2
                self.health += 7000
                Robot.terima_aksi(other,self.damage)
                self.damage = 5500
                return f"Lecalicus menambah darah sebanyak 7000 HP\n"
            else:
                Robot.terima_aksi(other,self.damage)
                return f"Lecalicus menambah darah sebanyak 4000 HP\n"

    def terima_aksi(self,damage):
        if damage > self.health :
            self.health = 0
            print(f"{self.nama} menerima damage sebesar {damage} DMG, sisa darah : {self.health} HP\n{self.nama} sudah mati!")
            Robot.alive = False
        else:
            self.health -= damage
            print(f"{self.nama} menerima damage sebesar {damage} DMG, sisa darah : {self.health} HP")

class Antares(Robot):
    def __init__(self):
        super().__init__("Antares", 50000, 5000)

class Alphasetia(Robot):
    def __init__(self):
        super().__init__("Alphasetia", 40000, 6000)

class Lecalicus(Robot):
    def __init__(self):
        super().__init__("Lecalicus", 45000, 5500)

print("Selamat datang di pertandingan robot Yamako")
robot_pilihan = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
while robot_pilihan <= 3 and robot_pilihan > 0:
    if robot_pilihan == 1:
        robotku = Antares()
        robot_pilihan = 0
    elif robot_pilihan == 2:
        robotku = Alphasetia()
        robot_pilihan = 0
    elif robot_pilihan == 3:
        robotku = Lecalicus()
        robot_pilihan = 0
    else: 
        print("Pilihan tidak tersedia!")
        robot_pilihan = input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): ")
robot_lawan = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): ")) 
while robot_lawan <=3 and robot_lawan >0:
    if robot_lawan == 1:
        robotmu = Antares()
        robot_lawan = 0
    elif robot_lawan == 2:
        robotmu = Alphasetia()
        robot_lawan = 0
    elif robot_lawan == 3:
        robotmu = Lecalicus()
        robot_lawan = 0
    else: 
        print("Pilihan tidak tersedia!")
        robot_lawan = input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): ")

print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting\n")
while Robot.alive:
    Robot.jumlah_turn += 1
    print(f"Turn saat ini: {Robot.jumlah_turn}")
    print(f"Robotmu ({robotku.nama} - {robotku.health} HP), robot lawan ({robotmu.nama} - {robotmu.health} HP)")
    pilihanku=int(input(f"Pilih tangan robotmu ({robotku.nama}): "))
    pilihan_lawan=random.randint(1, 3)
    print(f"Robot lawan {robotmu.nama} memilih : {pilihan_lawan}")

    if pilihanku == 1:
        if pilihan_lawan == 1:
            print("Seri!\n")
        elif pilihan_lawan == 2:
            print(Robot.lakukan_aksi(robotmu,robotku))
        elif pilihan_lawan == 3:
            print(Robot.lakukan_aksi(robotku,robotmu))
    elif pilihanku == 2:
        if pilihan_lawan == 1:
            print(Robot.lakukan_aksi(robotku,robotmu))
        elif pilihan_lawan == 2:
            print("Seri!\n")
        elif pilihan_lawan == 3:
            print(Robot.lakukan_aksi(robotmu,robotku))
    elif pilihanku == 3 :
        if pilihan_lawan == 1:
            print(Robot.lakukan_aksi(robotmu,robotku))
        elif pilihan_lawan == 2:
            print(Robot.lakukan_aksi(robotku,robotmu))
        elif pilihan_lawan == 3:
            print("Seri!\n")
print("Pertandingan berakhir!")
