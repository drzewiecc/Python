

# Uzytkownik podaje przesuniecie liter
przesuniecie = int(input("Wybierz przesuniecie w szyfrze: "))

# Uzytkownik wybiera, czy chce zaszyfrowac czy odszyfrowac informacje. Pyta do skutku.
dzialanie = input("Chcesz zakodowac czy odkodowac jakas informacje? (zakodowac/odkodowac) ")
while dzialanie!="zakodowac" and dzialanie!="odkodowac":
    dzialanie = input("Nie obsluguje takiej komendy. \nWybierz jeszcze raz: ")

#szyfrowanie --> funkcja
def szyfrowanie(przesuniecie):
    slowo = input("Podaj slowo ktore chcesz zaszyfrowac: ")
    litery = list(slowo)


#tworzenie slownika zawierajacego afbabet
alfabet = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j",
           11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s",
            20:"t", 21:"u", 22:"v", 23:"w", 23:"x", 24:"y", 25:"z" }
print(alfabet[23])
#Zrob przesuniecie key+przesuniecie