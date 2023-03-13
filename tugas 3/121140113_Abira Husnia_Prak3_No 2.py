#tugas prak 3 RB
#121140113 Abira Husnia

class AkunBank:
    list_pelanggan = {}  

    #constructor
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo) -> None:
        #private
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        AkunBank.list_pelanggan.update({self.__no_pelanggan:self.__nama_pelanggan})

    #fungsi lihat menu
    def lihat_menu(self):
        print(f"Selamat datang di Bang Juara\nHalo {self.__nama_pelanggan}, ingin melakukan apa?\n1. Lihat Saldo\n2. Tarik Tunai\n3. Transfer Saldo\n4. Keluar")
        choice=int(input("Masukkan Pilihan : "))
        print()
        if choice == 1:
            AkunBank.lihat_saldo(self)
        elif choice == 2:
            AkunBank.tarik_tunai(self)
        elif choice == 3:
            AkunBank.transfer(self)
        elif choice == 4:
            print(f"Terimakasih Sudah Melakukan Transaksi")
            exit()
        else:
            print("Inputan salah, Masukkan Pilihan!")
    
    #fungsi cek saldo
    def lihat_saldo(self):
        print(f"{self.__nama_pelanggan}, memiliki saldo Rp {self.__jumlah_saldo}\n")
        AkunBank.lihat_menu(self)

    #fungsi tarik tunai
    def tarik_tunai(self):
        while True:
            penarikan=int(input("Masukkan jumlah nominal yang ingin ditarik : "))
            if penarikan <= self.__jumlah_saldo:
                self.__jumlah_saldo-=penarikan
                print(f"\nSaldo berhasil ditarik!\nSisa saldo anda adalah Rp.{self.__jumlah_saldo}\n")
                break
            else:
                print(f"Nominal saldo yang Anda punya tidak cukup!")
        AkunBank.lihat_menu(self)
    
    #fungsi transfer
    def transfer(self):
        jumlah_transfer=int(input("Masukkan nominal yang ingin ditransfer : "))
        if jumlah_transfer <= self.__jumlah_saldo:
            no_rek = int(input("Masukkan no rekening tujuan : "))
            if no_rek in self.list_pelanggan:
                print(f"\nTransfer Rp.{jumlah_transfer} ke {self.list_pelanggan[no_rek]} sukses!\nSisa saldo anda adalah Rp.{self.__jumlah_saldo - jumlah_transfer}\n")
                AkunBank.lihat_menu(self)
            else:
                print(f"No rekening tujuan tidak dikenal! Kembali ke menu utama...")
                AkunBank.lihat_menu(self)
        else:
            print(f"Maaf, saldo anda tidak cukup. Kembali ke menu utama...")
            AkunBank.lihat_menu(self)
    
#objek
Akun1 = AkunBank(1234, "Abira Husnia", 5000000000) 
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

Akun1.lihat_menu()
