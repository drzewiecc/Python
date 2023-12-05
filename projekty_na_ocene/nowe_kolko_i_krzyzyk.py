print("Witaj w grze w kolko i krzyzyk!\nZasady sa proste-wybierasz pole za pomoca liczby, ktora jest oznaczone.")
print(" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 ")
print("Swoj ruch wykonujecie na zmiane.")
#jezeli pole_n=1 to znaczy, ze jest zajete przez kolko, 2 - zajete przez krzyzyk, jesli rowna sie 0 to jest wolne
pole=[0,0,0,0,0,0,0,0,0]
rzad1=[" - ","|"," - ","|"," - "]
rzad2=[" - ","|"," - ","|"," - "]
rzad3=[" - ","|"," - ","|"," - "]
while pole.count(0)>0:
    wybor_kolko=int(input("Kolko ---> wybierz pole: "))
    if wybor_kolko==1:
        pole[1]=1
        rzad1[1]=" o "
    if wybor_kolko==2:
        pole[2]=1
        rzad1[2]=" o "