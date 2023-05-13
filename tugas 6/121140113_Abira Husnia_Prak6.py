from abc import ABC, abstractmethod

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo

    def lihat_saldo(self):
        print(f"Saldo akun {self.nama}: Rp {self.saldo}")

    @abstractmethod
    def transfer_saldo(self, jumlah):
        pass

    @abstractmethod
    def lihat_suku_bunga(self):
        pass


class AkunGold(AkunBank):
    def transfer_saldo(self, jumlah):
        if self.tahun_daftar >= 3 and jumlah > 100000:
            print("Transfer berhasil. Biaya administrasi: Gratis")
        elif self.tahun_daftar < 3 and jumlah > 100000:
            print("Transfer berhasil.\nBiaya administrasi: Rp 2.000")
        else:
            print("Transfer berhasil.\nBiaya administrasi: Gratis")

    def lihat_suku_bunga(self):
        if self.tahun_daftar >= 3 and self.saldo >= 1000000000:
            print("Suku bunga bulanan: 1%\n")
        elif self.tahun_daftar < 3 and self.saldo >= 1000000000:
            print("Suku bunga bulanan: 2%\n")
        else:
            print("Suku bunga bulanan: 3%\n")


class AkunSilver(AkunBank):
    def transfer_saldo(self, jumlah):
        if self.tahun_daftar >= 3 and jumlah > 100000:
            print("Transfer berhasil. Biaya administrasi: Rp 2.000")
        elif self.tahun_daftar < 3 and jumlah > 100000:
            print("Transfer berhasil. Biaya administrasi: Rp 5.000")
        else:
            print("Transfer berhasil. Biaya administrasi: Gratis")

    def lihat_suku_bunga(self):
        if self.tahun_daftar >= 3 and self.saldo >= 10000000:
            print("Suku bunga bulanan: 1%")
        elif self.tahun_daftar < 3 and self.saldo >= 10000000:
            print("Suku bunga bulanan: 2%")
        else:
            print("Suku bunga bulanan: 3%")


# pengguna AkunGold
akun_gold = AkunGold("Abira", 2, 1500000000)
akun_gold.lihat_saldo()
akun_gold.transfer_saldo(300000)
akun_gold.lihat_suku_bunga()

# pengguna AkunSilver
akun_silver = AkunSilver("Husnia", 4, 3000000)
akun_silver.lihat_saldo()
akun_silver.transfer_saldo(100000)
akun_silver.lihat_suku_bunga()
