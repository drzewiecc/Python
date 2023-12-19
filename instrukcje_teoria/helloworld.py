print("Hello world")
a = 10
rzeczywista = 10.5
print(a)
print('%.20f'%rzeczywista)
tekst="hi"
tekst2='hello'
tekst3="hello 'world'"
print(tekst3)

# printowanie połączenia zmiennej i tekstu
print("Wartość zmiennej a to:", a)
print(f"Wartość zmiennej a to: {a}")
print("Wartość zmiennej a to %.2f"%a)
# str zmienia zmienną na tekst
print("Wartość zmiennej a to:" + str(a))

# wprowadzanie informacji
imie = input("Podaj swoje imię ")
wiek = int(input("Ile masz lat?"))
print("Cześć,", imie)
print("Masz", wiek, "lat.")

# importowanie bibliotek, robimy to na początku kodu u
import random
los=random.randint(1, 20)

import math
potega=math.pow(2, 3)
print(potega)

suma=2+5
roznica=9-8
iloczyn=7*8
iloraz=6/3
potega2=3**2
modulo=7%3

print("\ngithub")