#tugas prak 1 RB
#121140113 Abira Husnia

username = "informatika"
password = "12345678"

for i in range(3):
  us = str(input("Username anda : "))
  ps = str(input("Password anda : "))
  if us == username and ps == password:
    print("Berhasil login!")
    exit()
  elif i == 2 and (us != username or ps != password):
    print("Akun anda diblokir!")
  else:
    print("Username atau password salah coba lagi!")
  print()