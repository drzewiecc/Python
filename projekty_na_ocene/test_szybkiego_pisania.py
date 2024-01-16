import random
import time
konfiguracja=[]
wpisane=[]
alfabet = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j",
            11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s",
            20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}

def wpisywanie():
    for k in range(liczba_liter):
        wpisane.append(input("Podaj litere: "))

print("Witaj w tescie szybkiego pisania! Otrzymasz 20 konfiguracji zlozonych z losowych liter, ktore bedziesz musial przepisac.")
powtorzenia=5
liczba_liter=3
start=time.time()
#konfiguracje z trzema literami
for i in range(powtorzenia):
    for j in range(liczba_liter):
        konfiguracja.append(alfabet[random.randint(1,26)])
    print(konfiguracja)
    konfiguracja=konfiguracja
    #teraz urzytkownik wpisuje konfiguracje
    wpisywanie()
    if wpisane[0]==konfiguracja[0] and wpisane[1]==konfiguracja[1] and wpisane[2]==konfiguracja[2]:
        print("Ok, nastepna konfiguracja.")
        konfiguracja=[]
    else:
        print("Zle, jeszcze raz.")
        wpisywanie()
    konfiguracja=[]

#konfiguracje z czterema literami
liczba_liter=4
for i in range(powtorzenia):
    for j in range(liczba_liter):
        konfiguracja.append(alfabet[random.randint(1,26)])
    print(konfiguracja)
    konfiguracja=konfiguracja
    wpisywanie()
    if wpisane[0]==konfiguracja[0] and wpisane[1]==konfiguracja[1] and wpisane[2]==konfiguracja[2] and wpisane[3]==konfiguracja[3]:
        print("Ok, nastepna konfiguracja.")
        konfiguracja=[]
    else:
        print("Zle, jeszcze raz.")
        wpisywanie()
    konfiguracja=[]