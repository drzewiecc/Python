print("Tu mozesz przeliczyc jednostki masy, tempetarury i odleglosci.")
print("Jesli chcesz przeliczyc jednostki masy wpisz: 1\nJesli chcesz przeliczyc jednostki temperatury wpisz: 2\nJesli chcesz przeliczyc jednostki odleglosci wpisz: 3")
wybor=int(input())
while not wybor==1 or wybor==2 or wybor==3:
        print("Nie obsluguje takiej komendy.")
        wybor=int(input("Jeszcze raz: "))

if wybor==1:
    #masa
elif wybor==2:
    #temperatura
    print("Tu przeliczysz temperature wyrazona w stopniach Celcjusza na Fahrenheita lub na odwrot.")
    jednostka=input("Podaj jednostke (C/F), w ktorej wyrazona jest temperatura: ")
    while not wybor=="F" or wybor=="F":
        print("Nie obsluguje takiej komendy.")
        jednostka=int(input("Jeszcze raz: "))
    if jednostka=="C":
         wartosc=int(input("Podaj wartosc: "))
         print()
elif wybor==3:
    #odleglosc