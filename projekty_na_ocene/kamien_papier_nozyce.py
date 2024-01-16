import random
wg = 0
wk = 0
print("Witaj w grze kamien, papier, nozyce. Grasz do trzech wygranych.")
print("Wybierz swoj ruch wpisujac kamien, papier lub nozyce.")
ruchy=["kamien", "papier", "nozyce"]
wk=0
wg=0
wygrana=""
def gra():
    ruch_gracza=input("Twoj ruch: ")
    while not ruch_gracza=="kamien" and not ruch_gracza=="papier" and not ruch_gracza=="nozyce":
        ruch_gracza=input("Nie ma takiej opcji. Sproboj jeszcze raz: ")
    ruch_komp=ruchy[random.randint(0,2)]
    print("Ruch komputera: ", ruch_komp)
    if ruch_gracza==ruch_komp:
        print("Remis")
    elif ruch_gracza=="kamien" and ruch_komp=="papier":
        print("Komputer wygral.")
        wygrana="komp"
    elif ruch_gracza=="kamien" and ruch_komp=="nozyce":
        print("Gracz wygral.")
        wygrana="gracz"
    elif ruch_gracza=="papier" and ruch_komp=="kamien":
        print("Gracz wygral.")
        wygrana="gracz"
    elif ruch_gracza=="papier" and ruch_komp=="nozyce":
        print("Komputer wygral.")
        wygrana="komp"
    elif ruch_gracza=="nozyce" and ruch_komp=="kamien":
        print("Komputer wygral.")
        wygrana="komp"
    elif ruch_gracza=="nozyce" and ruch_komp=="papier":
        print("Gracz wygral.")
        wygrana="gracz"

while not wk==3 or wg==3:
    gra()
    if wygrana=="gracz":
        wg=wg+1
    else:
        wk=wk+1

if wg==3:
    print("Wygrales!!! Gratulacje :)")
else:
    print("Przegrales :(")

#Cos nie dziala przy wynikach