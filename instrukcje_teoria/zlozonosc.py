lista = [1,2,3,4,5,6,7,8,9,10]
for i in lista:
    print(i)

# obliczamy czas wykonania
import time
start=time.time()
lista2 = [100000,2,3,4, 5, 6, 7, 8, 9, 12, 123, 2345, 4567, 456, 23455, 12345567879, 9843758367, 32675892465982, 9999, 12567, 908076249, 8082763450, 13, 14, 16, 18, 112, 332, 445, 90, 90586]
for i in lista:
    print(i)

end=time.time()
print(end-start)

# zlozonosc kwadratowa
n=int(input("Podaj liczbę całkowitą: "))
start=time.time()
for i in range(n):
    for j in range(n):
        print("#", end='')
    print()

end=time.time()
print(end-start)