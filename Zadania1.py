import math


#Zadanie 1.1.1 
print(1+2+3+4+5+6)

#Zadanie 1.2.1
x = 3
y = 4
print(x, '+ ', end=' ')
print (y, x + y, sep=' = ')
print('x + y = ', x+y)

#Przyklad 2

def kwadrat(x):
 print(x * x)

print('7^2 = ', kwadrat(7))
print('(2+3)^2', kwadrat(2+3))


#Zadanie 2.1.1

def suma(x, y):
	print(x +y)

print('7 + 3 = ', suma(7,3))
print('8 + 6 = ', suma(8,6))

#Zadanie 2.1.2
#Lepsze zastosowanie do uzywania funkcji
def suma_return(x, y):
	return(x +y)

print('7 + 3 = ', suma_return(7,3))
print('8 + 6 = ', suma_return(8,6))

#Zadanie 2.1.3

def pole_kola(r):
	return(math.pi*r*r)

print('pole kola o promieniu 13 wynosi ', pole_kola(13))

#Zadanie 2.1.4
def reszta(x,y):
	print(x, ':', y, '\n', 'reszta z dzielenia wynosi ',x%y)
print(reszta(15,4))

#Zadanie2.1.5
def kwadrat_r(x):
 return(x * x)


def r_kwadratowe(a,b,c,x):

	d = kwadrat_r(x)
	return(a*d+b*x+c)
print('Wartosc funckji kwadratowej 2x^2+3x+7 dla x = 7 wynosi ',r_kwadratowe(2,3,5,7))
	
	
#Zadanie 2.2.1
for i in[1,2,3,4]:
	print(x, '^2 = ',x*x)

#Zadanie 2.3.1
sum = 0 	
for i in range(101):
	sum = sum + i*i
print('Suma kwadratow liczb od 1 do 100 wynosi ',sum)

#Zadanie 2.3.2

def sum_for(a,b):
	sum_f =0 
	for c in range(a+1,b):
		sum_f = sum_f +c
	return(sum_f)
print('Suma liczb calkowitych wiekszych od 5 a mniejszych od 10 ',sum_for(5,10))


#Zadanie 2.5.1
def znak(liczba):
	if liczba > 0 :
		print(abs(liczba), 'jest dodatnia')
	elif liczba < 0:
		print(abs(liczba), 'jest ujemna')
	else:
		print(abs(liczba),'nie jest dodatnia ani ujemna')
a=znak(5)
b=znak(-9)
c=znak(0)


#Zadanie 2.5.2
def wypisz(x):
	for i in range(21):
		if i%x != 0:
			print(i)

print(wypisz(4))
#Zadanie 2.6.1

def suma_while(a, b):
	x = a +1
	s =0
	while x > a and x <b:
		s = s + 1
		x = x +1
	return (s)
print(suma_while(2, 20))
			
#Zadanie 2.8.1
for m in range(9,100):
	if m%7 == 0:
		print( m, end = ' ')

#Zadanie 2.8.2

for i in range(7):
	print ('X'*i)

#LUB
for x in range(7):
	for y in range(x+1):
		print('X', end= ' ')
	print()
	
#Zadanie 2.8.3
for x in range(7):
	y = 0
	while y <=x:
		print('X', end= '')
		y = y+1
	print()
	
#Zadanie 2.8.4
def bezwzgledne(lista):
	for x in lista:
		if x > 0 :
			print(x, end= ' ')
		else:
			print(abs(x), end= ' ')
b=lista([5, -10, 15, 0])

#Zadanie 2.8.5

def trojkat(limit, x =0, napis= ""):
	if(x < limit):
		napis =napis + "X"
		print(napis)
		trojkat(limit, x+1, napis)
trojkat(7)

#lub

def trojkat2(limit, x =0):
	if(x < limit):
		for y in range(x+1):
			print("X", end= '')
		print()
		trojkat2(limit, x+1)
trojkat2(7)

#Zadanie 2.8.6
def tylko_wtedy(a,b):
	if a == b:
		return(a,' jest rownowazne ',b)
	else:	
		return(a,' nie jest rownowazne ',b)
tylko_wtedy(True, False)
tylko_wtedy(True, True)

#Zadanie 2.8.7

def xor(a, b):
	return a != b
def xor(a, b):
	return a ^ b
c =xor(5,6)

#Zadanie 2.8.8

def implikacja(a, b):
	if a:
		return b
	return True
	
#lub

def implikacja2(a,b):
	return not a or b
	
d=implikacja(True, False)
e=implikacja2(True, True)


			
