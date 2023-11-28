print("Witaj w grze w kolko i krzyzyk!\nZasady sa proste-wybierasz pole za pomoca liczby, ktora jest oznaczone.")
print(" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 ")
print("Swoj ruch wykonujecie na zmiane.")
#jezeli pole_n=1 to znaczy, ze jest zajete przez kolko, 2 - zajete przez krzyzyk, jesli rowna sie 0 to jest wolne
pole=[0,0,0,0,0,0,0,0,0]
while pole.count(0)>0:
    wybor_kolko=int(input("Kolko ---> wybierz pole: "))