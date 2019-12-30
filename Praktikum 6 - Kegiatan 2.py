# Program Akun
# Dibuat Oleh Baihaqi L200190169
import random
Angka = random.randint(0,1000)

Nama = 'Baihaqi Fatah Muhammad'
TanggalLahir = '29 Juni 2001'


Nama_Singkat = ((Nama[0]) + '. ' + (Nama[8]) + '. ' + (Nama[-8:]))
Username = ((Nama[0]) + (TanggalLahir[0:2]) + (TanggalLahir[-4:]))
Password = ((Nama[0:3]) + str(Angka))


print(Nama)
print(TanggalLahir)
print(Nama_Singkat)
print(Username)
print(Password)
