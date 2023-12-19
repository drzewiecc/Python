# instrukcje warunkowe
liczba=int(input("Podaj liczbe: "))

if liczba>0 :
    print("Liczba jest wieksza od zera.")
elif liczba==0:
    print("Liczba jest rowna zeru.")
else:
    print("Liczba jest mniejsza od zera.")

# petla for
for i in range(3):
    print("Numer: ", i)

# printuje tylko liczby podzielne przez 2
for i in range(1, 100):
    if i%2==0:
        print(i)

# Wypisuje co 2 (krok petli)
for i in range(1, 101, 2):
    print(i)

# Ujemny krok petli
for i in range(100, 0, -1):
    print(i)

# Przechodzi po kazdej literce po kolei
# Przerywa petle po pierwszym o
for litera in "slowo":
    if litera=="o":
        break
    print(litera)

# Przechodzi po kazdej literce po kolei
# Przeskakuje jedna z literacji petli(taki skip)
for litera in "slowo":
    if litera=="o":
        continue
    print(litera)


# petla while
liczba2=int(input("Podaj liczbe: "))

while liczba<0:
    liczba2=int(input("Podaj liczbe jeszcze raz: "))

print("\ngithub")