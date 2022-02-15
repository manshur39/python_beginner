


from ntpath import altsep


print ('hello world, saya akan mempelajari python dengan sungguh-sungguh!')
a=10;b=9;c=1
print(a+b+c)
print('')
#kita bisa memecah satu statement panjang menjadi multiple baris dengan tanda backslah(\)
print('Fungsi backslash (\) :')
kondisi = 10<5 and 10>9 or 11 == 6+5 and 0 ==100*5/(25-15)
kondisi = 10<5\
    and 10>9\
    or 11 == 6 + 5\
    and 0 == 100 * 5 / (25-15)
#comment
#komentar satu baris menggunakan tanda (#), Contoh:
# variabel a mempresentasikan panjang
a = 5
b= 10 #variabel b mempresentasikan tinggi
"""dan variabel c mempresentasikan luas
persegi dari hasil perkalian 
variabel a dan variabel b
"""
c=a*b
print (c)
#Belajar Variabel dan tipe data:
nama = "Nurul Huda"
usia = 25
sudah_menikah = True
print("nama :", nama)
print("usia :", usia)
print("sudah Menikah :", sudah_menikah)
#beberapa variabel dan nilai dalam satu baris (multiple) :
a,b,c = 1,2,"mantap"
print("a:", a)
print("b:", b)
print("c:", c)
#kita juga bisa menambahkan satu nilai yang sama untuk
#beberapa variabel
d=e=f=10
print("d:", d)
print("e:", e)
print("f:", f)
#fungsi type() untuk memeriksa tipe data pad python
a = "Madura"
b = 50
print(type(a))
print(type(b))
#belajar jenis tipe data pada python
#tipe data numerik
panjang = 5
lebar = 10.5
luas = panjang * lebar
print(luas)
print(panjang, '*', lebar,'=', luas)
print('Tipe dari variabel panjang:', type(panjang))
print('Tipe dari variabel lebar:', type(lebar))
print('Tipe dari variabel luas:', type(luas))
#tipe data numerik
a = 5j
b = 10j
c = a + b
print (a, '+', b, '=', c)
print ('Tipe dari a: ', type(a))
print('Tipe dari b: ',type(b))
print('Tipe dari c: ', type (c))
#Tipe data string (Teks)
nama_depan = 'Wahit'
nama_belakang = 'Abdulloh'
nama_lengkap = nama_depan +' '+ nama_belakang
usia = '12'
alamat = 'Bangkalan'
kata_mutiara = "Don't judge a book by it's cover"
print(nama_lengkap,',', 'usia:', usia,',', 'dari: ', alamat,',','kata mutiara: ', kata_mutiara)
print('\nTipe dari nama_lengkap: ', type(nama_lengkap))
print('Tipe dari usia: ',type(usia))
print('Tipe dari alamat: ', type(alamat))
print('Tipe dari kata_mutiara: ', type(kata_mutiara))
#Tipe data boolean (Benar/Salah)
saya_orang_indonesia = True
saya_robot = False
print('apakah saya orang indonesia?', saya_orang_indonesia)
print('Apakah saya adalah robot?', saya_robot)
print('Tipe dari saya_orang_indonesia', type(saya_orang_indonesia))
print('Tipe dari saya_adalah_robot', type(saya_robot))
#Tipe data koleksi
#Tipe data list
#List kosong
list_kosong = []
#List yang berisi kumpulan string
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']
#list yang berisi kumpulan integer
list_nilai = [60,70,80,90]
#list campuran berbagai tipe data 
list_campuran = [150, 33.33, 'Presiden Sukarno', False]
print('list_kosong:',list_kosong)
print('list_buah:',list_buah)
print('list_nilai:',list_nilai)
print('list_campuran:',list_campuran)
#indexing isi list
print(list_buah[0])
print(list_buah[1])
print(list_buah[2])
print(list_buah[3])
#indexing negatif isi list
print(list_buah[-1])
print(list_buah[-2])
print(list_buah[-3])
print(list_buah[-4])
#Slicing list
list_buah = ['Pisang', 'Nanas','Melon','Durian']
print(list_buah[0:1])
print(list_buah[0:4])
print(list_buah[0:3])
print(list_buah[-3:-1])
#Slicing tanpa batas
print(list_buah[0:])
print(list_buah[1:])
print(list_buah[2:])
print(list_buah[ :4])
print(list_buah[ :3])
#Mengubah data dalam list
list_buah = ['Pisang','Nanas','Melon', 'Durian']
print(list_buah)
#Ubah data pertama
list_buah[0] = 'Jeruk'
print(list_buah)
#Ubah data terakhir
list_buah[-1] = 'Mangga'
print(list_buah)
#Ubah data dalam range 
list_buah[1:3] = ['Naga', 'Pepaya']
print(list_buah)
#menambah item ke dalam list .append()
list_buah = ['Jeruk', 'Naga', 'Pepaya', 'Mangga']
list_buah.append('Sirsak')
print(list_buah)
#menambah data di index manapun dalam list .insert()
list_buah.insert(0,'Jambu')
print(list_buah)
list_buah.insert(4, 'Manggis')
print(list_buah)
#menghapus item dalam list
#menggunakan fungsi .pop()
list_angka = [1,2,3,4,5]
print(list_angka)
#hapus satu angka dibelakang
angka_yang_terhapus = list_angka.pop()
print('angka_yang_terhapus:', angka_yang_terhapus)
print(list_angka)
#menggunakan fungsi .remove()
list_buah2=['Mangga', 'Jeruk', 'Jambu', 'Sirsak']
print(list_buah2)
list_buah2.remove('Jambu')
print(list_buah2)
list_buah2.insert(0, 'Mangga')
print(list_buah2)
list_buah2[0] = 'Apel'
print(list_buah2)
#menggunakan statement del
print('\n' * 2)
list_buah3 = ['Mangga','Jeruk', 'Jambu','Jeruk']
print(list_buah3)
del list_buah3[1]
print(list_buah3)
del list_buah3[0:2]
print(list_buah3)
#menggabungkan dua buah list atau lebih
a= [1,2,3]
b=['a']
c=[True,'b',False]
listBaru = a+b+c
print(listBaru)
#mengurutkan data
list_buah = ['Mangga','Jeruk','Zaitun','Apel','Durian']
print(list_buah)
#Urutkan secara ascending
list_buah.sort()
print(list_buah)
list_buah.reverse()
print(list_buah)
#Tipe data tuple
#penulisan tipe data tuple
#cara standar:
tuple_jenis_kelamin = ('laki-laki','perempuan')
#tanpa kurung:
tuple_status_perkawinan = 'menikah','lajang'
#menggunakan fungsi tuple:
tuple_lulus = tuple(['lulus','tidak lulus'])
#tuple kosong:
tuple_kosong = ()
#tuple hanya berisi satu item:
tuple_tunggal = (10,) #diharuskan menulis tanda koma agar isi variabel dianggap tipe data tuple
#cara mengakses/indexing nilai tuple
#cara standar
tuple_jenis_kelamin = ('laki-laki','perempuan')
print(tuple_jenis_kelamin[1]) #indeks satu
print(tuple_jenis_kelamin[0]) #indeks nol
#negatif indeks
print(tuple_jenis_kelamin[-2])
print(tuple_jenis_kelamin[-1])
#slicing tuple
tuple_buah=('Pisang','Nanas','Melon','Durian')
print(tuple_buah[0:1])
print(tuple_buah[0:2])
print(tuple_buah[1:3])
print(tuple_buah[0:-1])
print(tuple_buah[-1:-3])
print(tuple_buah[-2:-1])
print(tuple_buah[-3:-1])
#slicing tanpa batas:
tuple_buah=('Pisang','Nanas','Melon','Durian')
print(tuple_buah[0:])
print(tuple_buah[1:])
print(tuple_buah[2:])
print(tuple_buah[3:])
print(tuple_buah[ :0])
print(tuple_buah[ :1])
print(tuple_buah[ :2])
print(tuple_buah[ :3])
print(tuple_buah[ :4])
#Sequence unpacking
siswa = ('Nurul Huda', 'Bangkalan', 24)
#ekstrak data/sequence unpacking
nama,asal,usia = siswa
#setiap variabel diatas akan memiliki nilai dari tiap isi tuple 
#secara berurutan
print('Nama:', nama)
print('Asal:', asal)
print('Usia:', usia)
#menggabungkan dua buah tuple atau lebih
a = (1,2,3)
b = (50,60,70)
c= a + b
print(c)
#fungsi-fungsi bawaan tuple (len(), max(), min())
nilai_semester1 = (80,90,100,88,60)
#Fungsi max() = mencari nilai paling besar dari sebuah tuple
max(nilai_semester1)
print(max(nilai_semester1)) 
#fungsi min() : Mencari nilai paling kecil dari sebuah tuple
min(nilai_semester1)
print(min(nilai_semester1))
#fungsi len (menghitung jumlah item pada tuple)
len(nilai_semester1)
print(len(nilai_semester1))
#Operator pada python
#Operator Aritmatika : untuk menghitung operasi matematika
#Contoh:
a,b=10,3
print(a,'+',b,'=',a+b) #penjumlahan
print(a,'-',b,'=',a-b) #pengurangan
print(a,'*',b,'=',a*b) #perkalian
print(a,'/',b,'=',a/b) #pembagian
print(a,'%',b,'=',a%b) #modulus
print(a,'**',b,'=',a**b) #perpangkatan
print(a,'//',b,'=',a//b) #pembagian bulat
#Operator komparasi atau perbandingan
#Contoh:
a, b = 5, 10
print(a,'>',b,'=',a>b) #operator lebih dari
print(a,'<',b,'=',a<b) #operator kurang dari
print(a,'==',b,'=',a==b) #operator sama dengan
print(a,'!=',b,'=',a!=b) #operator tidak sama dengan
print(a,'>=',b,'=',a>=b) #operator lebih dari sama dengan
print(a,'<=',b,'=',a<=b) #operator kurang dari sama dengan
#Operator penugasan
#Contoh:
#penugasan pertama
a=10
print('a = 10 ->', a)
a+=5
print('a += 5 ->', a)
a-=2
print('a -= 2 ->', a)
a*=10
print('a *= 10 ->', a)
a /= 10
print('a/=10 ->', a)
#karena a jadi float, kita ubah lagi menjadi integer
a =int(a)
a %= 7
print('a %= 7 ->', a)
a //= 2
print('a //= 2 ->', a)
a **= 10
print('a **= 10 ->', a)
a &= 10
print('a &= 10 ->', a)
a |= 10
print('a |= 10 ->', a)
a ^=10
print('a ^= 10 ->', a)
a >>= 10
print('a >>= 10 ->', a)
a<<=10
print('a <<= 10 ->', a)
#Operator Logika
#operator ini mengembalikan nilai dengan tipe data boolean
#Contoh:#and #or #not
print(True and True)
print(1 + 2 == 3 and True)
print('------')
print(False or 1>5)
print(False or 5>2)
print('------')
print(not(1 > 5))
print(not(1<5))
#Operator keanggotaan
#Contoh: #in #not in
perusahaan = 'Microsoft'
list_pulau = ['Jawa','Sumatera','Sulawesi']
mahasiswa = {'nama': 'Lendi Fabri', 'asal' : 'Lamongan'}
print("apakah 'c' ada di variabel perusahaan : ", 'c' in perusahaan)
print("apakah 'z' tidak ada di variabel perusahaan : ", 'z' not in perusahaan)
print("Apakah 'Madura' ada di variabel list_pulau?", 'Madura' in perusahaan)
print("Apakah 'Madura' tidak ada di variabel list_pulau?", 'Madura' not in perusahaan)
print("Apakah atribut 'nama' ada di variabel mahasiswa? ", 'nama' in mahasiswa)
#Operator Identitas
#Contoh : #is #is not
a=5
b=5
list_a = [1,2,3]
list_b = [1,2,3]
nama_a = 'budi'
nama_b = 'budi'
#output True
print('a is b :', a is b)
#output False
print('a is not b: ', a is not b)

#output False
print('list_a is list_b:', list_a is list_b)
#Output True
print('list_a == list_b:', list_a == list_b)

#Output True
print('nama_a is nama_b:',nama_a is nama_b)
#Output False
print('nama_a is not nama_b: ', nama_a is not nama_b)
#Cek id atau lokasi penyimpanan suatu nilai pada python
print(id("merah"))
print(id("merah"))
print(id(10))
print(id(10))
#Operator bitwise
#bitwise : operator yang berhubungan dengan angka-angka biner
#biner dari angka 0
print(format(0, '08b'))
#biner dari angka 1
print(format(1, '08b'))
#biner dari angka 2
print(format(2,'08b'))
#biner dari angka 3
print(format(3, '08b'))
#biner dari angka 4
print(format(4,'08b'))
#contoh operator bitwise:
a = 1
b = 64
print('a =', a,'=',format(a, '08b'))
print('b =', b,'=',format(b, '08b'), '\n')

print('[and]')
print('a & b =', a&b)
print(format(a, '08b'),'&',format(b,'08b'),'=',format(a&b,'08b'),'\n')

print('[or]')
print('a|b =',a|b)
print(format(a,'08b'),'|',format(b,'08b'),'=',format(a | b,'08b'),'\n')

print('[xor]')
print('a ^ b =',a ^ b)
print(format(a, '08b'),'^',format(b,'08b'),'=',format(a ^ b,'08b'),'\n')

print('[not]')
print('~a ~b =', ~a,~b)
print('~'+ format(a,'08b'),'~' + format(b,'08b'),'=',format(~a,'08b'),format(~b,'08b'),'\n')

print ('[shift right]')
print('a >> b =', a >> b)
print(format(a,'08b'),'>>',format(b,'08b'),'=',format(a >> b,'08b'),'\n')

print('[shift left]')
print('b << a =', b << a )
print(format(b,'08b'),'<<',format(a,'08b'),'=',format(b << a,'08b'),'\n')
#Mengambil input pada python
#Fungsi input()
#Contoh:
#nama = input('Masukan nama anda: ')
#print('Halo', nama,'..selamat datang! :)')
#konversi tipe data string ke integer:
#print('Kalkulator luas persegi panjang\n')
#panjang = input ('Masukan panjang: ')
#lebar = input ('Masukan lebar: ')
#print('Luas =',int(panjang) * int(lebar))

#Menampilkan Output
#Fungsi #print #format, dll
#Pemisah pada fungsi print 
#parameter #sep (separator)
#Contoh:
print('Andi','Budi','Tasya','Lala', sep='__')
#parameter #end
print('Merkurius', end='><')
print('Venus', end= '><')
print ('Bumi', end='><''\n')
print('asep')
print('Ujang')
print('Bambang')
#Menggunakan #sep dan #end secara bersamaan
print('1','2','3', sep='*', end='^^''\n')
#Memformat Output
#menggunakan fungsi str.format()
#Contoh:
a=5
b=3
print('{} + {}  = {}'.format(a,b,a+b))
#Format dengan index
#Contoh:
print ('{} dan {}'.format('Huda','Budi'))
#Contoh dengan index:
print('{1} , {0} , {3} dan {2}'.format('Huda','Budi','Asep','Ujang',),'\n')
#Format dengan kunci
print('Halo {nama_depan} {nama_belakang}'
.format(nama_depan='Agus',nama_belakang= 'Priyono'))
#Begini juga bisa
print('Halo {nama_depan} {nama_belakang}'
.format(
    nama_belakang='Priyono',
    nama_depan ='Agus'
)
)

#BAB 9 : Percabangan (if-elif-else)
if True :
    print('kode program ini akan di eksekusi')
if False :
    print('kode program ini tidak akan di eksekusi')
print('kode program ini akan selalu di eksekusi karena tidak masuk dalam percabangan.')
#Contoh penggunan ekspresi logika:
if 5 > 10: #False
    print('Nilai 5 lebih dari 10')
if 10 > 5 : #True
    print('Nilai 10 lebih dari 5')
#blok if..else :
nilai = 50
print('Nilai anda adalah:',nilai,'\n')

if nilai >= 70:
    print('Selamat anda LULUS!')
else:
    print('Maaf anda TIDAK LULUS!')
#Menambahkan fungsi input
# nilai = int(input('masukan nilai anda: '))
# print('Nilai anda adalah:',nilai,'\n')

# if nilai >= 70:
    # print('Selamat anda LULUS!')
# else:
    # print('Maaf anda TIDAK LULUS!')

#Blok if..elif..else
#menggunakan metode input data : 
# nama,nilai = input('masukan nama Siswa: '), int(input('masukan nilai hasil ujian: '))
# print ('nama siswa:',nama,'\n''hasil ujian:', nilai)
nama,nilai = 'Asep', 89
print('Nama Siswa:',nama,'\n''nilai ujian:',nilai)
if nilai >= 90:
    print('Predikat A')
elif nilai >= 80<90:
    print('Predikat B')
elif nilai >= 60<80:
    print('Predikat C')
elif nilai >= 40<60:
    print('Predikat D')
else :
    print('Predikat E')
#Percabangan dengan operator-operator
#Contoh untuk operator keanggotaan
# buah_yang_tersedia = ['jeruk','mangga','melon']
# buah_yang_dicari = input('masukan nama buah dalam huruf kecil:  ')

# if buah_yang_dicari in buah_yang_tersedia:
    # print ('Buah yang anda cari tersedia')
# else:
    # print('buah yang anda cari tidak tersedia')

#Percabangan satu baris:
hasil_ujian = 79
#Contoh dengan fungsi input:
# nilai = int(input('masukan nilai: '))
status = 'Lulus' if hasil_ujian >=75 else 'tidak lulus'
print (status)

#Percabangan Bertingkat:
nilai = 78
usia = 16
# contoh dengan fungsi input :
# nilai = int(input('masukan nilai: '))
# usia = int(input('masukan usia: '))

if nilai >=70 :
    if usia > 15 :
        print('selamat kak, kakak lulus!''\n')
    else :
        print('selamat dek, adek lulus!''\n')
else :
    if usia > 15 :
        print ('maaf kak, kakak tidak lulus!''\n')
    else :
        print ('maaf dek, adek belum lulus!''\n')

#BAB 10: Perulangan for
#Contoh:
listKota = ['Jakarta','Surabaya','Depok','Bekasi','Solo','Jogjakarta','Semarang','Makassar']

for kota in listKota:
    print(kota,'\n')

#mengetahui urutan iterasi for dengan list
#menggunakan fungsi #enumerate

for i, kota in enumerate (listKota):
    print(i,kota, sep='.''\n')

#for dengan fungsi range()
#Contoh buat perulangan >> ## 0 sampai 4
for i in range (5):
    print('perulangan ke: ', i)

#contoh lain
for i in range (10,15):
    print('i=',i) 

print('\n')

#contoh bilangan genap kelipatan 2
for i in range(2,12,2):
    print ('i=',i)

print('\n')

#contoh bilangan ganjil
for bilangan_ganjil in range (1,10,2):
    print(bilangan_ganjil)
print('\n')

#for dengan tuple
tupleBuah = ('Mangga','Jeruk','Pepaya','Apel')

for buah_buahan in tupleBuah:
    print (buah_buahan)
print('\n')

#for dengan string
for i, karakter in enumerate ('Indonesia ID'):
    print (i, karakter,sep=' > ')
print('\n')
#for...break & continue
#contoh continue:
for i in range(10,20):
    if (i == 17):
        continue
    print (i)
print('\n')
#Fungsi break
#contoh break:
for i in range(10,20):
    if(i == 17):
        break
    print(i)
print('\n')

#for...else + break
#contoh:
list_kota = ['Jakarta', 'Surabaya', 'Depok']
#menggunakan fungsi input
#kota_yang_dicari = input('masukan nama kota yang kamu cari: ')
kota_dicari = 'Jakarta'
for i, kota in enumerate(list_kota):
    #kita ubah katanya ke lowercase 
    #agar menjadi case sensitive
    if kota.lower() == kota_dicari.lower():
        print('Kota yang anda cari berada pada indeks ke : ', i)
        break
else:
    print('Kota yang anda cari tidak ditemukan')
print('\n')
deret_angka = (10,13,18,19)
for i in deret_angka:
    if i %2==0 :
        print('genap',i)
    else :
        print('ganjil',i)
print('\n')

#BAB 11 : Perulangan While
#contoh:
i = 1
while i <=10:
    print (i)
    i +=1
print ('\n')
#perulangan while untuk list
#fungsi len()
nama_kota = ['Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar']
i=0
while i <len(nama_kota):
    print(nama_kota[i])
    i+=1
print('\n')
#fungsi .pop()
i = 0
while nama_kota:
    print(nama_kota.pop(0))
    i+=1

#perulangan while dengan inputan

"""Contoh : Perhatikan contoh di bawah. Pada contoh ini 
kita akan meminta user untuk memasukkan angka ganjil lebih dari 50. 
Jika user justru memasukkan nilai genap atau nilai yang kurang dari 50, 
maka sistem akan meminta user untuk menginputkan kembali.""" 

a = 79
#dengan fungsi input
# a = int(input('Masukan angka ganjil lebih dari 50: '))
while a%2 !=1 or a<=50:
    a = int(input('Salah, masukan lagi: '))
print('Benar')
print('\n')
#perulangan while dengan continue
nama_kota = ['Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar']
#skip jika i adalah bilangan genap
#dan i lebih dari 0
i=-1
while i < len(nama_kota):
    i+=1
    if i %2 == 0 and i > 0 :
        print('skip')
        continue
    #tidak di eksekusi ketika continue dipanggil
    print(nama_kota[i])
print('\n')

#Perulangan while dengan break
nama_kota = ['Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar']
kotaYangDicari = 'semarang'
#dengan fungsi input
# kotaYangDicari = input('Masukkan nama kota yang dicari: ')

i = 0
while i < len(nama_kota):
  if nama_kota[i].lower() == kotaYangDicari.lower():
    print('Ketemu di index', i)
    break

  print('Bukan ', nama_kota[i])
  i += 1


#perulangan while dengan else
nama_kota = ['Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar']
kotaYangDicari = 'ciamis'
#dengan fungsi input
# kotaYangDicari = input('Masukkan nama kota yang dicari: ')

i = 0
while i < len(nama_kota):
  if nama_kota[i].lower() == kotaYangDicari.lower():
    print('Ketemu di index', i)
    break

  print('Bukan ', nama_kota[i])
  i += 1
else:
    print('maaf kota yang anda cari tidak ditemukan')

#BAB 12: Perulangan Bersarang / Bertingkat
#Alur Dasar:
for i in range(3):
    print('Perulangan luar [i]=', i)

    for j in range(5):
        print('perulangan dalam [i,j]= ', str(i)+','+str(j))
#Contoh lain

for baris in range (4):
    print('O',end=' ')
    for kolom in range (5):
        print('X', end=' ')
    else:
        print(' ')
#Menggunakan while
#contoh1:
max_baris = 3
max_kolom = 4

baris = 0
while baris < max_baris:
  kolom = 0
  while kolom < max_kolom:
    print('o' if kolom <= baris else '+', end= ' ')
    kolom += 1
  else:
    print('wkwkw')
  baris += 1
 
#contoh2 :
list_kota = ['jakarta','surabaya','makassar']

for kota in list_kota:
    print(kota)

    list_tempat = ['taman','mall','lapangan']

    while list_tempat:
        print ('-->', list_tempat.pop(0))

#Contoh lain:

import re
list_kota4 =['Solo','Surabaya','Bekasi','Jakarta']
vokal_huruf =['a','i','u','e','o']

for kota in list_kota4:
    print('['+kota+']')

    for vokal in vokal_huruf:
        print('-->', re.sub('[aiueo]',vokal,kota))
print('\n')

#BAB 13: Tipe data set
#Cara membuat set
#Menggunakan kurung kurawal:
himpunan_siswa = {'Huda','Lendis','Wahid','Basith'}
print(himpunan_siswa)

#mengkonversi list ke dalam set:
himpunan_buah = set(['mangga','apel'])
print(himpunan_buah)

#set dengan tipe data yang berbeda-beda:
set_campuran = {'manusia','hewan',5,True,('A','B')}
print(set_campuran)
print('\n')

#Menambah anggota pada set:
#Menggunakan fungsi add()
himpunan_abjad = {'a','b','c'}
print(himpunan_abjad)

#>>> menambah anggota dengan add()
himpunan_abjad.add('d')
himpunan_abjad.add('e')

#menambah lebih dari satu anggota sekaligus
#dengan fungsi update()
himpunan_abjad.update({'f','g'})
#bisa juga dengan list
himpunan_abjad.update(['h','i'])

print(himpunan_abjad)
print('\n')

#Menghapus anggota :
#fungsi remove(nilai): Untuk menghapus nilai yang dicari. Jika nilai yang dicari tidak ada, maka akan error.
#fungsi discard(nilai): Untuk menghapus nilai yang dicari. Jika nilai yang dicari tidak ada, tidak akan error.
#fungsi pop(): Mengambil dan menghapus nilai yang ada di sebelah kiri.
#fungsi clear(): Menghapus semua anggota.

#praktek:
himpunan_data= {'maya','budi',100,('a','b'),False,True}
print(himpunan_data)
print('')
#akan error jika nilai 100 tidak ada dalam set
himpunan_data.remove(100)
print(himpunan_data)
print('')
#tidak akan error jika ('a','b') tidak ada dalam set
himpunan_data.discard(('a','b'))
print(himpunan_data)
print('')
#remove nilai yang ada di sebelah kiri:
nilaiYangDihapus = himpunan_data.pop()
print('nilaiYangDihapus= ', nilaiYangDihapus)
print(himpunan_data)
print('')
#hapus semua nilai
himpunan_data.clear()
print(himpunan_data)
print('')

#Fungsi keanggotaan pada set
#>>>Fungsi union (Gabungan)
#>>>Fungsi intersection (irisan)
#>>>Fungsi difference (selisih)
#>>>Fungsi symmetric difference (komplement)
#>>>Dll.

#praktek:
grup_smp = {'andi','budi','ratna','sari'}

grup_sma = {'putri','ratna','andi','agus'}

#operasi union :
#cara 1 dengan simbol pipe ( | )
print(grup_smp|grup_sma)
#cara 2 
print(grup_smp.union(grup_sma))
print('')

#operasi intersection :
#cara 1 menggunakan simbol ( & )
print(grup_smp & grup_sma)
#cara 2 
print(grup_smp.intersection(grup_sma))
print('')

#operasi difference
print('\nanggota grup smp yang bukan anggota grup sma')
#cara 1 menggunakan simbol ( - )
print(grup_smp - grup_sma)
#cara 2 
print(grup_smp.difference(grup_sma))
print('')
print('\ndibalik, anggota grup sma yang bukan anggota grup smp: ')
print(grup_sma - grup_smp)
print(grup_sma.difference(grup_smp))
print('')

#symmetric difference
print('\nanggota yang hanya ikut satu grup saja: ')
print(grup_sma.symmetric_difference(grup_smp))
print('')

#Menampilkan anggota set dengan perulangan for
himpunan_buah2an={'pepaya','apel','jagung','rambutan'}

for buah in himpunan_buah2an:
    print(buah)

