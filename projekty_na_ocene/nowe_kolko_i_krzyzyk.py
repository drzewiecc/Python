def print_plansza_kolko():    
    if wybor_kolko==1:
        pole[0]=1
        rzad1[0]=" o "
    elif wybor_kolko==2:
        pole[1]=1
        rzad1[2]=" o "
    elif wybor_kolko==3:
        pole[2]=1
        rzad1[4]=" o "
    elif wybor_kolko==4:
        pole[3]=1
        rzad2[0]=" o "
    elif wybor_kolko==5:
        pole[4]=1
        rzad2[2]=" o "
    elif wybor_kolko==6:
        pole[5]=1
        rzad2[4]=" o "
    elif wybor_kolko==7:
        pole[6]=1
        rzad3[0]=" o "
    elif wybor_kolko==8:
        pole[7]=1
        rzad3[2]=" o "
    elif wybor_kolko==9:
        pole[8]=1
        rzad3[4]=" o "


def print_plansza_krzyzyk():
    if wybor_krzyzyk==1:
        pole[0]=2
        rzad1[0]=" x "
    elif wybor_krzyzyk==2:
        pole[1]=2
        rzad1[2]=" x "
    elif wybor_krzyzyk==3:
        pole[2]=2
        rzad1[4]=" x "
    elif wybor_krzyzyk==4:
        pole[3]=2
        rzad2[0]=" x "
    elif wybor_krzyzyk==5:
        pole[4]=2
        rzad2[2]=" x "
    elif wybor_krzyzyk==6:
        pole[5]=2
        rzad2[4]=" x "
    elif wybor_krzyzyk==7:
        pole[6]=2
        rzad3[0]=" x "
    elif wybor_krzyzyk==8:
        pole[7]=2
        rzad3[2]=" x "
    elif wybor_krzyzyk==9:
        pole[8]=2
        rzad3[4]=" x "
     

print("Witaj w grze w kolko i krzyzyk!\nZasady sa proste-wybierasz pole za pomoca liczby, ktora jest oznaczone.")
print(" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 ")
print("Swoj ruch wykonujecie na zmiane.")
#jezeli pole_n=1 to znaczy, ze jest zajete przez kolko, 2 - zajete przez krzyzyk, jesli rowna sie 0 to jest wolne
pole=[0,0,0,0,0,0,0,0,0]
rzad1=[" - ","|"," - ","|"," - "]
rzad2=[" - ","|"," - ","|"," - "]
rzad3=[" - ","|"," - ","|"," - "]
while pole.count(0)!=1:
    wybor_kolko=int(input("Kolko ---> wybierz pole: "))
    while not pole[wybor_kolko - 1] == 0:
        print("To pole jest juz zajete.")
        wybor_kolko=int(input("Kolko ---> wybierz pole: "))
    print_plansza_kolko()
    print(*rzad1)
    print(*rzad2)
    print(*rzad3)
    wybor_krzyzyk=int(input("Krzyzyk ---> wybierz pole: "))
    while not pole[wybor_krzyzyk - 1] == 0:
        print("To pole jest juz zajete.")
        wybor_krzyzyk=int(input("Krzyzyk ---> wybierz pole: "))
    print_plansza_krzyzyk()
    print(*rzad1)
    print(*rzad2)
    print(*rzad3)
print("Koniec petli")
wybor_kolko=int(input("Kolko ---> wybierz pole: "))
while not pole[wybor_kolko - 1] == 0:
    print("To pole jest juz zajete.")
    wybor_kolko=int(input("Kolko ---> wybierz pole: "))
print_plansza_kolko()
print(*rzad1)
print(*rzad2)
print(*rzad3)
print("Calkiem koniec")

#zrob sprawdzanie kto wygral, jesli pole[x]=1 i pole[y]=1 i pole[z]=1 itd.