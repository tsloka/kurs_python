import math


### PRZYKLADY

x ='A'
a, b, c = 'Ala', "ma", " kota i psa"
d = """...a co ma ...
	"kotek" ? """

print(x, a[2])
print(c[1], c[-1], c[-3])
print (a + b)
print ( 3 * a )
print(a + " " + b + c + d )

tekst = 'Python'
dlugosc = len(tekst)
print(dlugosc, tekst[2:6], tekst[3:], tekst[:3])

tekst2 = '123456789'
dlugosc2 = len(tekst2)
print(tekst2[::2], tekst2[1::2])
print(tekst2[::-1], tekst2[::-3])
print(tekst2[::-1][::3], tekst2[::3][::-1])



#Napis jako lista

for l in 'Abc' :
	print('litera', end = ' ')
	print(l)
#
s, ns = "abcdefgh", " "
#s[2] = "X"
s1 = s[:2] + "X" + s[3:5] +s[6:]


print(s)
print(s1)

for z in s:
	if z in "cf":
		ns = ns + "X"
	else:
		ns =ns + z
print(ns)


#Zadanie 3.1.1
def wspak(lista):
	for word in lista:
		print(word[::-1], end = " ")

a = wspak(['Ala', 'ma' , 'dwa', 'kotki'])


# Zadanie 3.1.2
def wyiks(zdanie):
	ns = " "
	for slowo in zdanie:
		if slowo in "0123456789,.:;/":
			ns = ns + slowo
		elif slowo in "QWERTYUIOPASDFGHJKLZXCVBNM":
			ns = ns + "X"
		else:
			ns = ns + "x"
	print(ns)
q = wyiks("Backport of mainline CPython 2.6/2.7 to old versions of Windows 9x/NT.")
print('\n')

#Zadania 3.2.1

def toStr(liczba, podstawa):
	napis = ""
	while liczba:
		cyfra = liczba % podstawa
		liczba = liczba // podstawa
		if cyfra < 10:
			napis = str(cyfra) + napis
		else:
			napis =chr(55 + cyfra) + napis
	return napis

print(toStr(761813, 2))
print(int('10111001111111010101', 2))

#KONWERSJA LICZBA - NAPIS

#szesnastkowo 
h1, h2, h3 = 0x1F, int("0x1F", 0), int("1F", 16)
#oktalnie
o1, o2, o3 = 0o17, int("0o17", 0), int("17", 8)
#binarnie
b1, b2, b3 = 0b101, int("0b101", 0), int("101", 2)

print("", h1, o1, b1, "\n", h2, o2, b2, "\n", h3, o3, b3)

#KODOWANIE ZNAKOW

w = "aąbcć ... " 
inUTF7 = w.encode('utf7')
inUTF8 = w.encode() #or w.encode('utf8')
print("'" + w + "' w UTF7 to: " + str(inUTF7) + ", w UTF8: " +str(inUTF8))

print("zdekodowany UTF7: " + inUTF7.decode('utf7'))

import codecs
b64 = codecs.encode(inUTF8, 'base64')
print("napis w UTF8 po zakodowaniu base64 to: " +str(b64))


#Zadanie 3.3.1
zakodowane = b'UHl0aG9uIGplc3QgZmFqbnkg8J+Yjg==\n'
zakodowane = codecs.decode(zakodowane, 'base64')
zakodowane =zakodowane.decode()
print(zakodowane)


#Wyrazenia regularne

import re

y = "aa bb cc bb ff bb ee"
x = "aa bb cc dd ff gg ee"

if re.match(".*[dz]", y):
	print("y zawiera d lub z")
if re.match(".*[dz]", x):
	print("y zawiera d lub z")
if re.match(".* ([a-z]{2}) .* \\1",y):
	print("y zawiera dwa razy to samo")
if re.match(".* ([a-z]{2}) .* \\1",x):
	print("z zawiera dwa razy to samo")

#zastepowanie
print(re.sub('[bc]+', "XX", y, 2))
print(re.sub('[bc]+', "XX", y))

#zachlannosc
print (re.sub('bb (.*) bb', "X \\1 X", y))
print (re.sub('.*bb (.*) bb.*', " \\1 ", y))
print (re.sub('.*?bb (.*) bb.*', " \\1 ", y))


#Zadanie 3.4.1
def czy_slowo(slowo):
	if re.match(".* [^ ]", slowo):
		print(slowo, " posiada spacje")
	else:
		print(slowo, "nie posiada spacji")
#lub

def spr(x):
	if re.match("[^ ]*$", x):
		print(x, "jest slowem")
	else:
		print(x, "nie jest slowem")
r = czy_slowo("defeaf ev")
f = czy_slowo("alamakota")
g = spr("defeaf ev")
h = spr("alamakota")

#Zadanie 3.4.2
def liczba(slowo):
	if re.match("[+-]?[0-9.]+$", slowo):
		print("jest liczba")
	else:
		print("nie jest liczba")
		
j = liczba("rafddfa")
k = liczba("+9656")

#Zadanie 3.5.1

def skrot(lista):
	for word in lista:
		print(word[0] + '-' + word[-1] + ' (', end= '')
		print(len(word), end= '')
		print(')')
ICM = (['Interdyscyplinarne', 'Centrum', 'Modelowania', 'Komputerowego'])

print(skrot(ICM))

#Zadanie 3.5.2

def male(x):
	for s in x:
		for l in s:
			if l in 'qazwsxedcrfvtgbyhnujmiklop':
				print(l *2, end= '')
			else:
				print(l, end= '')
		print()
l = male(['Ala', 'ma', 'kot', 'i PIES ma Ale'])


#Zadanie 3.5.4
def sprawdz(x):
	if re.match(".*xyz$", x):
		print(x, "konczy sie na xyz")
	else:
		print(x, "nie konczy sie na xyz")
z = sprawdz("okokokoxyz")

#Zadanie 3.5.5

def jezyk(x):
	if re.match("(a*)b*\\1$", x):
		print(x, "nalezy do jezyka")
	else:
		print(x, "nie nalezy do jezyka")
c = jezyk("abba")

a, b, c = 1, 3.14, "Python"

print(a, type(a))
print(b, type(b))
print(c, type(c))
c = (a == 1)
print(c, type(c))

l = ['i', 'c', 0, 'm']
l[0] = "I"
del l[2]
print(l)

for i in range(len(l)):
	print(l[i])
	l[i] = "q"
print(l)

s = 'asdfghjkl'
l = list(s)
l[2] = "X"
del(l[5])
s = "".join(l)
print(s)

l =['i', 'm']
l.insert(1, 'c')
print(l)
l.reverse()
print(l)
l.sort()
print(l)


### STRING
#https://www.tutorialspoint.com/python/string_replace.htm

string = "this is string example....wow!!! this is really string"
print(string.replace("is", "was"))
print(string.replace("is", "was", 3))

#https://www.tutorialspoint.com/python/string_split.htm
string = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print(string.split( ))
print(string.split(' ', 1 ))

#Zadanie 4.3.1

def parse(x):
	t =x.replace("XY", " ")
	return t.split(':')
print(parse("Ala:maXYkotka:i inne:zwierzeta"))

#Zadanie 4.3.2
def sortowanie(x):
	x.sort()
	x.reverse()
	return x
print(sortowanie(['Agata', 'Lukasz', 'Mariusz', 'Szczepan', 'Igor', 'Michal', 'Konstanty']))


#Zadanie 4.3.3

def sortuj(lista):
	l = lista.copy()
	l.sort()
	return l
print(sortuj(['Agata', 'Lukasz', 'Mariusz', 'Szczepan', 'Igor', 'Michal', 'Konstanty']))


# SLOWNIKI

slownik = {"bd" : "xx", 5 : True, "a" : 11}
for klucz in slownik:
	print(klucz, "=>", slownik[klucz])

if "bd" in slownik:
	print("jest elementem slownika o kluczu 'bd'")
	del slownik['bd']
slownik[15] = True
slownik["a"] = "yy"
#for k,v in m.items():
#	print(k, "=>", v)


#https://www.tutorialspoint.com/python/dictionary_get.htm
dict = {'Name': 'Zabra', 'Age': 7}
print("Value", "Age",": ",  dict.get('Age'))
print("Value : ",  dict.get('Education', "Never"))

#ZAdanie 4.4.1

def zlicz(x):
	s = {}
	for e in x:
		s[e] = s.get(e, 0) +1
	for k in s:
		print(str(k) + " wystepuje " + str(s[k]) + " razy")
zlicz(["AX", "B", "AX"])


#Zadanie 4.4.2
def konwert(x):
	s={}
	for w in x:
		poz = w.find("=")
		s[w[0:poz]] = w[poz+1:]
	return s
print(konwert(["aa=13", "b=Ala=kot", "f=xyz"]))

mapa = {'5' : 3, 'bd' : 20, 'a' : 101}
lista = sorted(mapa.items())
print(lista)

def k(x):
	return x[1]
lista = sorted(mapa.items(), key=k)
print(lista)


#Funckja jako argument funckji

def dzialanie(operacja):
	if operacja == "dodaj":
		def f(a, b):
			return a+b
		return f
	elif operacja == "mnoz":
		def f(a, b):
			return a*b
		return f
def dwa(funkcja, argument):
	return funkcja(2, argument)
d = dzialanie("dodaj")
a = dwa(d, 11)
b = dzialanie("mnoz")(4,4)
print(a, b)

#Zadanie 4.5.1
def dzialanie_s(x):
	s = { "dodaj" : (lambda a, b: a + b), "mnoz" : (lambda a, b: a * b)}
	return s.get(x)

def dwa(funkcja, argument):
	return funkcja(2, argument)
d = dzialanie_s("dodaj")
a = dwa(d, 88)
b = dzialanie_s("mnoz")(4,5)
print(a, b)


#Zadanie 4.5.2

def wykonaj(lista, funckja):
	for x in lista:
		funckja(x)

print(wykonaj([1, 2, 3], print))
