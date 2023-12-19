# Funkcje
# Pisz na poczatku kodu

def powitanie():
    print("Hej!")

powitanie()

def powitanie_imienne(imie):
    print("Hej, ", imie)

powitanie_imienne("Jacek")

# Funkcja zwracajaca wartosc
def dzielenie(dzielna, dzielnik):
    if dzielnik==0:
        return
    else:
        return dzielna/dzielnik
    
print(dzielenie(5,2))
print(dzielenie(4,0))
iloraz=dzielenie(6,3)
print(iloraz)


# Tablice i listy
lista=[1,2,3,9,7,6]
print(lista)
# Wyswietla bez separatorow
print(*lista)
# Sami wybieramy separator
print(*lista, sep=";")

# Sprawdzanie typu zmiennej
print(type(lista))

# Porzadkowanie listy
lista.sort()
print(lista)

# Odwracanie listy
lista.reverse()
print(lista)

# Liczy wszystkie 3 w liscie
print(lista.count(3))

# Usuwanie konkretnej wartosci z listy
lista.remove(3)
print(lista)

# Dodawanie wybranego elementu
lista.apend(11)
print(lista)

# Wywolywanie elementow
print(lista[0])

# Sprawdzanie dlugosci listy
print(len(lista))

# Podmienianie konkretnego elementu na liscie
lista[3]=4

# Wypisywanie listy
for i in lista:
    print(i)


# Tuple ---> nie da sie zmieniac

# Definiowanie
tupla=(1,2,3)
print(tupla)
#lub
tupla2=1,2,3,4,5,"abc"
print(tupla2)

# tupla3=("abc") ----> to nie jest tupla, ale
tupla3=("abc",)

print(len(tupla2))

print("\ngithub")