#Video 2 : Basic operator and input 

#print('what is your name?')
#name = input()
#print("Hallo", name)

#aritmatika operator:
import string


num1= 20
num2 = 5
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print (num1 / num2)
print(num1 ** num2)
print(num1 % num2)
print(num1//num2)

#print("pick a number:")
# num1= input()
# print("prick another number:")
# num2= input()
# SUM = int(num1) + int(num2)
# print('Hasilnya:',SUM)

#Video 3 : Conditions ( >,<,==,!=,>=,<=)
a = 4
b = 3
print(a>b)
print (a<b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print('Hello' == 'Hello')
print('hello' == 'HELLO')
print(2+2 == 4)
print (3+2 == 6)

#Video 4 : IF_ELIF_ELSE
#menggunakan fungsi input:
# height = input()
height = 1.68
if float(height) <1 :
    print('You cannot ride, you are under 1m')
elif float(height) >2 :
    print ('You cannot ride, you are over 2m')
else : 
    print('You can ride')
#menentukan angka ganjil dan genap
angka = 9
if angka % 2 ==0 :
    print ('Angka genap')
else:
    print ('Angka ganjil')
print('\n')

#Video 5 : Chained conditionals and nested statements
y=2
x=6
if y ==2:
    if x ==3:
        print('y=2, x=3')
    else:
        print('y=2, x!=3')
else:
    print('x!=2, y!=3')

print('\n')

#Video 6: for loops
for x in range (10): #(stop)
    print(x,end=',')
print('\n')

for x in range (2,6): #(start,stop)
    print(x,end=',')
print('\n')

for x in range (3,20,2): #(start,stop,step)
    print(x,end=',')
print('\n')

#Video 7: While loops
loop = 4
while loop==4:
    password=input('insert your password: ')
    if password=='tmbahagia':
        break
print('\n')

#Video 8: List and tuple
#Tipe data list
fruits = ['apple','pear']
print(fruits)
print(fruits[1]) #mengambil isi item list/indexing
fruits.append('strawberry') #menambah item list
print(fruits)
fruits[1]='avocado' #mengubah isi item list
print(fruits)
print('\n')
#Tuple
color = (255,255,255)
position = (1,'two',3.0)
print(type(position))
print(type(color))
print('\n')

#Video 9: Iteration by item
buah_buahan = ['apel','alpukat','pepaya','pisang','jambu']
for buah in buah_buahan:
    print(buah)
#cara 2:
for buah in buah_buahan:
    if buah == 'alpukat':
        print('alpukat')
    else :
        print('bukan alpukat')
#cara 3:
for x in range(len(buah_buahan)):
    if buah_buahan[x] == 'pisang':
        print('ini pisang')
    else : 
        print('bukan pisang')
print('\n')

#Video 10: String methods
#split
text ='tes metod split'
print(text.split())
#strip
text2=   'hallo gugel'
print(text2.strip())
#upper, lower, len
text3 ='MuhaMMaD tM'
print(text3.upper())
print(text3.lower())
print(len(text3))
print('\n')
#Video 11: Slice operator
buahh = ['jeruk','apel','pisang','alpukat','naga']
teks = 'aku suka python'
print(buahh[0:4:2]) #[start:stop:step]
print(teks[3:8])
print(buahh[:3])
print(buahh[2:])
buahh[1:1]=['pepaya']
print(buahh)
print('\n')
#Video 12: Function
def addTwo(x):
   print(x + 2)
addTwo(5)

def dikurangDua(x):
    print(x-2)
dikurangDua(10)

def String():
    print('hai')
def tulisan(teks):
    print(teks)
String()
tulisan('my name is taufik')

def luasPpanjang(panjang,lebar):
    Luas = panjang*lebar
    return Luas
print(luasPpanjang(3,5))

def luasSegitiga(alas,tinggi):
    L = (0.5*alas*tinggi)
    print(L)
luasSegitiga(4,6)
print('\n')
#Video 13: How to read a text file
file = open('text.txt','r')
f = file.readlines()
print(f)
newtext=[]
for teks in f:
    newtext.append(teks.strip())
print(newtext)
print('\n')

#Video 14: How to write a text file
test1= open('menulis.txt','w')
test1.write('hallo\n')
test1.write('my name is tm,\n and now im learning how to write text file in pyhton')
test1.close()

#Video 15: Using .count() and .find()
tekss ='helooo'
print(tekss.find('e'))
print(tekss.count('o'))
teks5='lima ikan tenggiri + sepuluh telur ayam + satu kilogram engkol'
if teks5.count('+')>0:
    print('ada penambahan')
else:
    print('tidak ada penambahan')

#Video 16: Introduction to modular programming
import myModule
print(myModule.func(3))
print(myModule.newfunc(5))

#Video 17: Optional parameters
def fungsi1 (x=10, tekss='ganteng'): #fungsi default
    print (x)
    if tekss == '1':
        print('tekss is one')
    else:
        print('tekss is not one')
fungsi1() 
#fungsi non default
def fungsi1 (x, tekss):
    print (x)
    if tekss == '1':
        print('tekss is one')
    else:
        print('tekss is not one')
fungsi1(10, '1') 

