import random
lista=[]
wybor = input("Chcesz podac czy wylosowac liste? (podac/wylosowac): ")
while wybor!="podac" and wybor!="wylosowac":
        wybor = input("Nie obsluguje takiej komendy. \nWybierz jeszcze raz: ")

if wybor=="podac":
    dlugosc=int(input("Podaj jak dluga bedzie twoja lista: "))
    dlugosc=dlugosc-1
    while dlugosc>=0:
        dodane=int(input("Podaj element: "))
        lista.append(dodane)
        dlugosc=dlugosc-1
    print(lista)
else:
     dlugosc=random.randint(1, 21)
     dlugosc=dlugosc-1
     while dlugosc>=0:
        dodane=random.randint(1, 1001)
        lista.append(dodane)
        dlugosc=dlugosc-1
     print(lista)

for i in lista:
    for j in lista:
         a=i
         b=j
         if i>j:
              lista[j]=a
              lista[i]=b
         else:
              lista[j]=b
              lista[i]=a
print(lista)