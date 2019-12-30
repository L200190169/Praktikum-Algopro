Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Baihaqi Fatah Muhammad'
>>> Nim = 'L200190169'
>>> X = '1' + Nim[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> 
>>> type(a)
<class 'int'>
>>> #type berarti perintah untuk mendefinisikan tipe tersebut
>>> #bahwa tipe tersebut berupa integer
>>> 
>>> type(b)
<class 'int'>
>>> #berarti tipe dari data tersebut adalah integer
>>> 
>>> a / b
53.13636363636363
>>> #perintah tersebut menampilkan pembagian dari nilai X dengan Jumlah pada Nama
>>> 
>>> a // b
53
>>> #perintah tersebut menampilkan pembagian yang dibulatkan pada nilai X dengan Jumlah pada Nama
>>> 
>>> 10 * (a - 999)
1700
>>> #perntah tersebut menampilkan operasi bilangan aritmatika dimulai dari nilai a yaitu 1169 dikurangi dengan 999 dan hasilnya dikali dengan 10
>>> 
>>> b ** 2
484
>>> #perintah tersebut menampilkan nilai b yaitu 22 dan dipangkatkan dengan 2
>>> 
>>> a % b
3
>>> #perintah tersebut menampilkan sisa pembagian dari nilai a dan b
>>> 
>>> c = 12.5
>>> 
>>> type(c)
<class 'float'>
>>> #perintah tersebut menampilkan tipe dari type data dari c. float, yaitu bilangan pecahan
>>> 
>>> a / c
93.52
>>> #perintah tersebut menampilkan operasi pembagian dari nilai a yaitu 1169 dibagi dengan nilai c yaitu 12.5
>>> 
>>> a // c
93.0
>>> #perintah tersebut menampilkan operasi pembagian yang dibulatkan dari nilai a dan nilai c dengan a bertype integer dan c bertype float, maka hasilnya float
>>> 
>>> a % c
6.5
>>> #perintah tersebut menampilkan sisa hasil bagi antara nilai a dengan nilai c
>>> 
>>> c > b
False
>>> #perintah tersebut menampilkan operator perbandingan, data tersebut berarti nilai c lebih kecil dari nilai d karena menampilkan hasil false
>>> 
>>> type(c > b)
<class 'bool'>
>>> #perintah tersebut menampilkan kelas dari type data tersebut, dan kelas dari tipe data tersebut yaitu boolean atau perbandingan
>>> 
>>> a > b and b > c
True
>>> #printah tersebut menampilkan true and true, maka hasilnya true
>>> 
>>> a > 1100 or b < 10
True
>>> #perintah tersebut menampilkan true or false, maka hasilnya true
