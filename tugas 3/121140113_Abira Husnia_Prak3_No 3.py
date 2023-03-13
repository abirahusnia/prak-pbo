#tugas prak 3 RB
#121140113 Abira Husnia

class HandPhone:
  #constructor
  def __init__(self, merk, jenis, ram, harga) -> None:
    self.merk = merk
    self._jenis = jenis
    self._ram = ram
    self.__harga = harga

  #fungsi untuk menampilkan spesifikasi
  def spesifikasi (self):
    print(f"\nMerk HP : {self.merk} \nJenis   : {self._jenis} \nRAM     : {self._ram} \nHarga   : {self.__harga}")

  #fungsi untuk mengubah harga
  def mengubah_harga(self, harga):
    self.__harga = harga

#objek
hp = HandPhone ("Samsung", "Z Fold 4 5G", "12 GB", 26999000)

print(f"Merk HP : {hp.merk}")
print(f"Jenis   : {hp._jenis}")
print(f"RAM     : {hp._ram}")
hp.spesifikasi()

hp.mengubah_harga("24999000")
hp.spesifikasi()
