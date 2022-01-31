


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