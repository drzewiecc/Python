# slowniki

kontakty={}
kontakty["Jan"] = 1234567890
kontakty["Romus"] = 9876543210

# bardziej zwiezla forma, po ostatnim elemencie nie dajemy przecinka
kontakty={
    "Adam": 3345,
    "Basia": 8878,
    "Janusz": 9009
}

# wyswietlanie ---> gdy wpiszemy nawiasy kwadratowe podpowiada elementy
print(kontakty["Janusz"])

# za pomoca petli ---> %s imie, %d numer (wyswietla "klucz" i "wartosc" w takiej kolejnosci --> jakies wartosci, tak jak w slownikach)
for imie, numer in kontakty.items():
    print("%s ma numer: %d" %(imie, numer))

# wyswietlamy tylko klucze lub tylko wartosci
print(kontakty.keys())
print(kontakty.values())

# usuwanie elementow
del kontakty["Jacek"]

print("\ngithub")