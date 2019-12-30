Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Baihaqi Fatah Muhammad'
>>> NIM = 169
>>> Tinggi = 1.65
>>> Berat = 60
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> 
>>> type(Aku)
<class 'tuple'>
>>> #perintah tersebut menampilkan kelas. Kelas tersebut adalah tuple yaitu deretan huruf atau deretan objek
>>> 
>>> Aku[0]
2001
>>> #perintah tersebut menampilkan slicing dari tipe data tuple "Aku", pengambilan tersebut menampilkan tahun lahir yang berada di dalam "Aku"
>>> 
>>> a = NIM % 4; Aku[a]
60
>>> #perintah tersebut menampilkan sisa pembagian antara 169 dengan 4, maka hasil dari Aku[a] yaitu 60
>>> 
>>> type(Aku[a])
<class 'int'>
>>> #perintah tersebut menampilkan kelas dari data "Aku[a]"
>>> 
>>> Aku[a:4]
(60, 1.65, 169)
>>> #perintah tersebut menampilkan data "Aku" yaitu Berat, Tinggi, NIM
>>> 
>>> type(Aku[4])
<class 'str'>
>>> #perintah tersebut menampilkan data ke 4 dari "Aku", yaitu Nama, bentuk data dari Nama adalah string
>>> 
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # perintah tersebut menampilkan eror karena kelas tuple tidak dapat dibuat untuk menyimpan data
>>> 
>>> type(Data)
<class 'list'>
>>> #program tersebut menampilkan jenis dari objek Data adalah list
>>> 
>>> type(Data[4])
<class 'str'>
>>>  #perintah tersebut menampilkan data ke 4 dari "Data", yaitu Nama, bentuk data dari Nama adalah string
>>> 
>>> Data[4][5]
'q'
>>> #perintah tersebut mengambil di dalam list selanjutnya mengambil lagi di dalam Nama di urutan ke 5
>>> 
>>> Data[4][a:6]
'aihaq'
>>> #perintah tersebut mengambil dari data Nama dan mengambil dari data ke 1 sampai ke 5
>>> 
>>> Data[0] = 'ok'; Data
['ok', 60, 1.65, 169, 'Baihaqi Fatah Muhammad']
>>> #perintah tersebut menambahkan string ke dalam list dan memanggil list tersebut
>>> 
>>> Data[-a]
'Baihaqi Fatah Muhammad'
>>> #perintah tersebut menampilkan Nama yang tersimpan di dalam list
>>> 
>>> range(a)
range(0, 1)
>>> #perintah tersebut menampilkan range dari a yatu 0 dan 1
